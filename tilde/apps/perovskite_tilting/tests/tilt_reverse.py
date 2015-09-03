#!/usr/bin/env python

# Euler tilting angles extraction reverse test
# First, distort on the known angle, then extract tilting and check if it is the same
# Author: Evgeny Blokhin

import os
import sys
import math
import random
from numpy import array

import set_path
from tilde.core.api import API
from tilde.parsers import Output
from tilde.core.constants import Perovskite_Structure
from tilde.apps.perovskite_tilting.perovskite_tilting import Perovskite_tilting # for limits

from ase import Atoms
from ase.lattice.spacegroup import crystal


# first, work with ASE
# this is the cubic perovskite given in orthorhombic P n m a, in order to allow arbitrary octahedral tilting
# NB: in Euler notation delta is gamma, delta plus/minus phi is alpha
# or in another terminology: phi is gamma, phi plus/minus psi is alpha

a = round(random.uniform(3.5, Perovskite_tilting.OCTAHEDRON_BOND_LENGTH_LIMIT*2), 3)

phi = round(random.uniform(0, Perovskite_tilting.MAX_TILTING_DEGREE), 3)
theta = round(random.uniform(0, Perovskite_tilting.MAX_TILTING_DEGREE), 3)
psi = round(random.uniform(0, Perovskite_tilting.MAX_TILTING_DEGREE), 3)

perovskite = crystal( \
            [random.choice(Perovskite_Structure.A),
            random.choice(Perovskite_Structure.B),
            random.choice(Perovskite_Structure.C),
            random.choice(Perovskite_Structure.C)],
            [(0.5, 0.25, 0.0), (0.0, 0.0, 0.0), (0.0, 0.25, 0.0), (0.25, 0.0, 0.75)],
            spacegroup=62, cellpar=[a*math.sqrt(2), 2*a, a*math.sqrt(2), 90, 90, 90])

# NB: perovskite.rotate_euler(phi=math.radians(phi), theta=math.radians(theta), psi=math.radians(psi))
# does not suit because of spatial orientation!
perovskite._masked_rotate(center=array([a*math.sqrt(2)/2, a, a*math.sqrt(2)/2]), axis='y', diff=math.radians(phi), mask=[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1])
perovskite._masked_rotate(center=array([a*math.sqrt(2)/2, a, a*math.sqrt(2)/2]), axis='x', diff=math.radians(theta), mask=[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1])
perovskite._masked_rotate(center=array([a*math.sqrt(2)/2, a, a*math.sqrt(2)/2]), axis='y', diff=math.radians(psi), mask=[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1])

# second, incorporate ASE into tilde
work = API()
virtual_calc = Output() # we always consider "calculation" while using tilde
virtual_calc.structures = [ perovskite ]
virtual_calc, error = work.classify(virtual_calc)
if error:
    raise RuntimeError(error)
virtual_calc = work.postprocess(virtual_calc)
is_perovskite = ('perovskite' in virtual_calc.info['tags'])

print "Test object:", virtual_calc.info['standard']
print "Is perovskite?", is_perovskite
if is_perovskite:
    print "Octahedra tilted on:", phi, theta, psi
    print "Extracted tilting is:", virtual_calc.apps['perovskite_tilting']['data']
