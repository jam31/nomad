
# ORM tools
# Idea by Fawzi Mohamed
# Author: Evgeny Blokhin

import os, sys
import httplib2
import bcrypt
from urllib import urlencode


class UniqueMixin(object):
    @classmethod
    def unique_filter(cls, query, *arg, **kw):
        raise NotImplementedError()

    @classmethod
    def as_unique(cls, session, *arg, **kw):
        return _unique(session, cls, cls.unique_filter, cls, arg, kw)

    @classmethod
    def as_unique_todict(cls, session, *arg, **kw):
        return _unique_todict(session, cls, cls.unique_filter, arg, kw)

def _unique(session, cls, queryfunc, constructor, arg, kw):
    '''
    https://bitbucket.org/zzzeek/sqlalchemy/wiki/UsageRecipes/UniqueObject
    Checks if ORM entity exists according to criteria,
    if yes, returns it, if no, creates
    '''
    with session.no_autoflush:
        q = session.query(cls)
        q = queryfunc(q, *arg, **kw)
        obj = q.first()
        if not obj:
            obj = constructor(*arg, **kw)
            session.add(obj)
    return obj

def _unique_todict(session, cls, queryfunc, arg, kw):
    '''
    Checks if ORM entity exists according to criteria,
    if yes, returns it, if no, returns dict representation
    (required for further DB replication and syncing)
    '''
    q = session.query(cls)
    q = queryfunc(q, *arg, **kw)
    obj = q.first()
    if not obj:
        obj = kw
        obj['__cls__'] = cls.__mapper__.class_.__name__
    return obj

def get_or_create(cls, session, defaults=None, **kwds):
    result = session.query(cls).filter_by(**kwds).first()
    if result:
        return result, False
    newVals=defaults
    if defaults is None:
        newVals={}
    newVals.update(kwds)
    result = cls(**newVals)
    session.add(result)
    session.flush()
    return result, True

def correct_topics(session, model, calc_id, cid, new_topics, mode, topics_hierarchy):
    assert model.Calculation.__tablename__

    found_entity = None
    for e in topics_hierarchy:
        if e['cid'] == cid:
            found_entity = e
            break
    assert found_entity, "Wrong topic identifier!"

    if isinstance(calc_id, (str, unicode)):
         calc_id = [calc_id]
    assert isinstance(calc_id, list)
    if isinstance(new_topics, (str, unicode)):
         new_topics = [new_topics]
    assert isinstance(new_topics, list)

    if mode == 'REPLACE':
        _replace_topics(session, model, calc_id, cid, new_topics)
    elif mode == 'APPEND':
        assert found_entity.get('multiple', False)
        _append_topics(session, model, calc_id, cid, new_topics)

def _replace_topics(session, model, calc_id, cid, new_topics):
    new_terms = []
    for new_topic in new_topics:
        new_term, created = model.get_or_create(model.uiTopic, session, cid=cid, topic=new_topic)
        new_terms.append(new_term)
    session.commit()

    for checksum in calc_id:
        for tid in session.query(model.tags.c.tid).join(model.uiTopic, model.tags.c.tid == model.uiTopic.tid).filter(model.uiTopic.cid == cid, model.tags.c.checksum == checksum).all():
             session.execute(model.delete(model.tags).where(model.and_(model.tags.c.checksum == checksum, model.tags.c.tid == tid[0])))
        session.commit()

        for new_term in new_terms:
            session.execute(model.insert(model.tags).values(checksum=checksum, tid=new_term.tid))
        session.commit()

def _append_topics(session, model, calc_id, cid, new_topics):
    new_terms = []
    for new_topic in new_topics:
        new_term, created = model.get_or_create(model.uiTopic, session, cid=cid, topic=new_topic)
        new_terms.append(new_term)
    session.commit()
    for new_term in new_terms:
        for checksum in calc_id: # .values([model.tag(checksum=checksum, tid=new_term.tid) for checksum in calc_id])
            try: session.execute(model.insert(model.tags).values(checksum=checksum, tid=new_term.tid))
            except model.IntegrityError:
                logger.critical("The pair (%s, %s) is already present in the tags table!" % (checksum, new_term.tid))
                session.rollback()
    session.commit()

def syncdb(slugs, model_scope=globals(), sync_setup={}):
    '''
    Sends all the given ORM items to the master,
    where they are saved, augmented with the IDs and sent back.
    @returns synced ORM items, error
    '''
    to_do, ready = [], []
    for slug in slugs:
        if isinstance(slug.__class__, DeclarativeMeta):
            ready.append(slug)
        elif isinstance(slug, dict):
            to_do.append(slug)
        else:
            logger.critical("Wrong ORM data format provided!")
            return None, "Wrong ORM data format provided!"

    if not to_do: return ready, None

    if isinstance(sync_setup['password'], unicode): sync_setup['password'] = sync_setup['password'].encode("ascii")

    pwhash = bcrypt.hashpw(sync_setup['password'], bcrypt.gensalt())
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'X-hash': pwhash.encode('utf-8')}
    body = urlencode({'to_sync': json.dumps(to_do)})

    h = httplib2.Http()
    try: resp, content = h.request(sync_setup['url'], "POST", body, headers=headers)
    except:
        logger.critical("Network error while requesting %s" % sync_setup['url'])
        return None, "Network error while requesting %s" % sync_setup['url']

    if resp.status != 200:
        logger.critical(str(content))
        return None, str(content)

    try: done = json.loads(content)
    except:
        logger.critical("Invalid sync data received!")
        return None, "Invalid sync data received!"

    for ormrepr in done:
        clsname = ormrepr['__cls__']
        ormrepr.pop('__cls__')
        ready.append(getattr(model_scope, clsname)(**ormrepr))

    return ready, None
