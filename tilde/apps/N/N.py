
# Tilde API demo
# calculates the ratio N between dimensions and number of atoms
# Author: Evgeny Blokhin

import os, sys
import math

from ase.data import chemical_symbols, covalent_radii
from tilde.core.common import ModuleError

R_ADDON = 0.5

class N():
    # this determines how the data should be represented in a table cell
    @staticmethod
    def cell_wrapper(obj):
        selfname = __name__.split('.')[-1]
        if not selfname in obj['apps']:
            return "<div class=tiny>n/a</div>"
        return "<i>%s</i>" % obj['apps'][selfname]

    # this is a main class code
    def __init__(self, tilde_calc):
        self.N = 0
        
        if tilde_calc['structures'][-1].periodicity == 3:
            self.N = tilde_calc['structures'][-1].dims
        
            #self.N = tilde_calc['structures'][-1].dims / len(tilde_calc['structures'][-1])

            for a in tilde_calc.structures[-1]:
                if not a.symbol in chemical_symbols:
                    raise ModuleError('Unexpected atom has been found!')
                    
                radius = covalent_radii[ chemical_symbols.index( a.symbol ) ]
                valence_zone = 4/3 * math.pi * (radius + R_ADDON)**3
                self.N -= valence_zone
                
        self.N = round(self.N)        
