'''
Created on 2 Mar 2014

@author: samgeen
'''

import sys, inspect, time
import LevelData, Eat, Talk, Use, Get
        
game = None


# VERB ACTIONS

jumpdead = '''The cybertower is high. So very high. You jump to your doom.
Cyberhackers will pass the browning, tentacled spray of 
blood and offal, skirting to avoid getting any on their shoes. If only you had some way of defying gravity itself.'''

jumplive = '''You float gently down to the cyberstreets below. Cyberpigeons nesting in neon-flecked crevices watch in bemusement as you pass.'''

jumpnull = '''You do a little jig on the spot. Yehaw!'''

holidaydead = '''Stressed out by the cyberlife of the hacker, you book a pleasant two week getaway in the Bahamas. On the beach
one day, you come across a strange shell. As you bend down to pick up the shell, a shark leaps out of the water, inches across the beach with its flippers, and 
tears you apart with its razor-sharp teeth. Later, the shark is killed by heavy metal poisoning from your implanted hackerdeck. Such is the cycle of life.'''

        
savetext = '''You feel a slight judder, then nothing, the world slipping back into place, unchanged. 
You tap your pockets; everything is there, even your haxsnax. And yet - somehow the world feels safer, like you could leap from the tallest
cyberscraper and wake up the next morning, right as rain. You smile, and hum the theme tune to Deus Ex.'''
        
loadtext = '''The world shudders, the sky turning to wireframe, then vanishing, a wall of black rushing to greet you and-'''
        
def jump():
    '''
    Leap!
    '''
    if game.Level().Name() == "intro":
        if not "antigravity" in sys.modules.keys():
            print game.ParseText(jumpdead)
            game.Restart()
        else:
            print game.ParseText(jumplive)
            game.ChangeLevel(LevelData.streets)
    else:
        game.ParseText(jumpnull)
        
def leap():
    '''
    Jump!
    '''
    jump()
        
def look():
    '''
    Inspect your surroundings! Examine for clues!
    '''
    print game.ParseText(game.Level().Look())
    
def holiday():
    '''
    A soothing beach vacation
    '''
    print game.ParseText(holidaydead)
    game.Restart()
    
def vacation():
    '''
    A relaxing seaside holiday
    '''
    holiday()
    
def hubris():
    '''
    Win the game instantly with one cunning move
    '''
    print game.ParseText(game.Level().Death())
    game.Restart()
    
def talk(thing):
    '''
    If only you could talk to the monsters OWAIT-
    '''
    Talk.talk(thing)
    
def eat(thing):
    '''
    Eat this thing in your inventory! Why not! What could go wrong?
    NOTE: Objects in your inventory are strings, so remember to add quotation marks!
    '''
    Eat.eat(thing)
    
def use(thinga, thingb):
    '''
    Use thinga on thingb. Or is it thingb on thinga? No, it's thinga on thingb. I think.
    NOTE: Objects in your inventory are strings, so remember to add quotation marks!
    '''
    Use.use(thinga, thingb)
    
def get(thing):
    '''
    Get the thing. Get it! Put it in your inventory.
    '''
    Get.get(thing)
    
def save(filename="savefile"):
    '''
    Save the game state
    Input: save file name (default: "savefile")
    '''
    print game.ParseText(savetext)
    game.Save(filename)

def load(filename="savefile"):
    '''
    Load the game state from a savefile
    Input: save file name (default: "savefile")
    '''
    print game.ParseText(loadtext)
    game.Load(filename)
    time.sleep(2)
    print game.ParseText(game.Level().Text())
    
def exit():
    '''
    Get out of here! Remember to save first, B. T. Dubs.
    '''
    game.Exit()
    
#def __str__(self):
#    return str(dir(self))