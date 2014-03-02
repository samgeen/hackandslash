'''
Created on 2 Mar 2014

@author: samgeen
'''

import sys

jumpdead = '''The cybertower is high. So very high. You jump to your doom.
Cyberhackers will pass the browning, tentacled spray of 
blood and offal, skirting to avoid getting any on their shoes.'''

class Verbs(object):
    def __init__(self, game):
        self._game = game
        
    def jump(self, punk):
        if not "antigravity" in sys.modules.keys():
            print self._game.ParseText(jumpdead)
            self._game.Restart()
            
    def look(self, punk):
        print self._game.ParseText(self._game.Level().Look())