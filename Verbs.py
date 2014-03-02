'''
Created on 2 Mar 2014

@author: samgeen
'''

import sys, inspect
import LevelData

jumpdead = '''The cybertower is high. So very high. You jump to your doom.
Cyberhackers will pass the browning, tentacled spray of 
blood and offal, skirting to avoid getting any on their shoes. If only you had some way of defying gravity itself.'''

jumplive = '''You float gently down to the cyberstreets below. Cyberpigeons nesting in neon-flecked crevices watch in bemusement as you sail down to the cybercrete pavement.'''

holidaydead = '''Stressed out by the cyberlife of the hacker, you book a pleasant two week getaway in the Bahamas. On the beach
one day, you come across a strange shell. As you bend down to pick up the shell, a shark leaps out of the water, inches across the beach with its flippers, and 
tears you apart with its razor-sharp teeth. Later, the shark is killed by heavy metal poisoning from your implanted hackerdeck. Such is the cycle of life.'''

class Verbs(object):
    def __init__(self, game):
        self._game = game
        
    def jump(self, punk):
        if not "antigravity" in sys.modules.keys():
            print self._game.ParseText(jumpdead)
            self._game.Restart()
        else:
            print self._game.ParseText(jumplive)
            self._game.ChangeLevel(LevelData.streets)
            
    def leap(self, punk):
        self.jump(punk)
            
    def look(self, punk):
        print self._game.ParseText(self._game.Level().Look())
        
    def holiday(self, punk):
        print self._game.ParseText(holidaydead)
        self._game.Restart()
        
    def vacation(self, punk):
        self.holiday(punk)
        
    def hubris(self, punk):
        print self._game.ParseText(self._game.Level().Death())
        self._game.Restart()
        
    def __str__(self):
        return str(dir(self))