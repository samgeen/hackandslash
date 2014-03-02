'''
Created on 2 Mar 2014

@author: samgeen
'''

import sys, inspect
import LevelData
        
game = None


# VERB ACTIONS

jumpdead = '''The cybertower is high. So very high. You jump to your doom.
Cyberhackers will pass the browning, tentacled spray of 
blood and offal, skirting to avoid getting any on their shoes. If only you had some way of defying gravity itself.'''

jumplive = '''You float gently down to the cyberstreets below. Cyberpigeons nesting in neon-flecked crevices watch in bemusement as you pass.'''

holidaydead = '''Stressed out by the cyberlife of the hacker, you book a pleasant two week getaway in the Bahamas. On the beach
one day, you come across a strange shell. As you bend down to pick up the shell, a shark leaps out of the water, inches across the beach with its flippers, and 
tears you apart with its razor-sharp teeth. Later, the shark is killed by heavy metal poisoning from your implanted hackerdeck. Such is the cycle of life.'''

talkmute = "This thing can't talk. Or maybe it can, but doesn't want to. Either way."
        
def jump():
    if not "antigravity" in sys.modules.keys():
        print game.ParseText(jumpdead)
        game.Restart()
    else:
        print game.ParseText(jumplive)
        game.ChangeLevel(LevelData.streets)
        
def leap():
    jump()
        
def look():
    print game.ParseText(game.Level().Look())
    
def holiday():
    print game.ParseText(holidaydead)
    game.Restart()
    
def vacation():
    holiday()
    
def hubris():
    print game.ParseText(game.Level().Death())
    game.Restart()
    
def talk(thing):
    try:
        print game.ParseText(thing.Talk())
    except:
        print game.ParseText(talkmute)
    
def __str__(self):
    return str(dir(self))