'''
Created on 5 Mar 2014

@author: samgeen
'''

game = None

'''
cyberogres
t-rex
llama
haxsnax
sword
player
'''

def examine(thing):
    strthing = str(thing)
    if not _checkexists(strthing):
        print game.ParseText("That thing doesn't seem to exist. Weird.")
        return
    elif strthing == "cyberogres" or strthing == "t-rex" or strthing == "llama":
        print game.ParseText(thing.Examine())
    elif strthing == "player":
        print game.ParseText("You are the sexy, quick-thinking hacker $PLAYERNAME")
    elif strthing == "haxsnax":
        print game.ParseText("Tasty tasty haxsnax. Made for hackers, by hackers, out of used circuitboards.")
    elif strthing == "sword":
        print game.ParseText("A sharp cybersword. You swoosh it in your hand. It makes a \"schiwing!\" sound.")
    else:
        print game.ParseText("For some reason I can't tell you what this is. It's a "+strthing+". So OK.")  
    
def _checkexists(strthing):
    for item in game.Vars():
        if str(item) == strthing:
            return True
    for item in game.Inventory():
        if str(item) == strthing:
            return True:
    return False