
# tries to find vacancy defects

import os
import sys
import fractions


# hierarchy API: __order__ to apply classifier and __properties__ extending basic hierarchy
__order__ = 20
__properties__ = [ {"category": "vacancy content", "source": "vac", "order": 13, "negative_tagging": True, "has_column": True, "has_label": True, "descr": ""} ]

def classify(tilde_obj):
    ''' detect vacant places of host atoms '''
    if len(tilde_obj.info['elements']) < 2: return tilde_obj
    elif tilde_obj.structures[-1]['periodicity'] in [0, 1, 2]: return tilde_obj
    tilde_obj.info['expanded'] = reduce(fractions.gcd, tilde_obj.info['contents'])
    if sum(tilde_obj.info['contents']) / tilde_obj.info['expanded'] < 15: return tilde_obj # check for >= 15-atoms
    
    gcds = []
    for i in range(1, 3): # max 2 missing atoms of THE SAME type
        for index in range(len(tilde_obj.info['contents'])):
            chk_content = []
            chk_content.extend(tilde_obj.info['contents'])
            if tilde_obj.info['lack']: try_index = tilde_obj.info['elements'].index(tilde_obj.info['lack'])
            else: try_index = index
            chk_content[try_index] += i
            gcds.append([try_index, i, reduce(fractions.gcd, chk_content)])
            if tilde_obj.info['lack']: break
    m_red = max(gcds, key = lambda a: a[2]) # WARNING: only one of several possible reducing configurations is taken!
    
    #print tilde_obj.info['formula']
    #print "--->", m_red
    
    # this structure probably contains defects
    if m_red[2] > tilde_obj.info['expanded']:
    
        # check reasonable defect concentration (more than 25% is not a defect anymore!)
        c = float(m_red[1]*100) / m_red[2]
        if c > 25: return tilde_obj
        
        tilde_obj.info['expanded'] = m_red[2]        
        
        tilde_obj.info['contents'][ m_red[0] ] += m_red[1]
        for n, i in enumerate(map(lambda x: x/tilde_obj.info['expanded'], tilde_obj.info['contents'])):
            if i>1: tilde_obj.info['standard'] += tilde_obj.info['elements'][n] + str(i)
            else: tilde_obj.info['standard'] += tilde_obj.info['elements'][n]
            if n == m_red[0]:
                if i==1: tilde_obj.info['standard'] += '1-d'
                else: tilde_obj.info['standard'] += '-d'
                tilde_obj.info['properties']['vac'] = '%2.2f' % c + '%'
        tilde_obj.info['tags'].append('vacancy defect')
        
    return tilde_obj
    