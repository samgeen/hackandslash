'''
Created on 5 Mar 2014

@author: samgeen
'''

import webbrowser
import Animals, Talk
game = None

# Things that could be in the world:
# cyberogres
# llama
# trex

text = {}
text["null"] = "I can't see that thing. Are you sure that thing exists, $PLAYERNAME? I'm not. Let's pretend you didn't do that."
text["player"] = "You climb into your inventory. It's cosy in here!"
text["trex"] = "The trex climbs into your inventory, apparently. I'm not even sure what's happening any more."
text["llama"] = "You pick up the llama and put it in your inventory, because this is an adventure game and I don't know."
text["cyberogres"] = "In this case 'get' means 'acquire', not 'attack'. And they don't look too keen on being acquired."
text["fail"] = "Sorry, $PLAYERNAME, I can't let you do that."

def get(thing):
    try:
        strthing = str(thing)
    except:
        strthing = "null"
    if not _checkexists(strthing):
        print game.ParseText(text["null"])
        return
    if strthing in text:
        if strthing == "llama" or strthing == "player":
            print game.ParseText(text[strthing])
            MoveToInventory(thing)
        if strthing == "cyberogres":
            print game.ParseText(text[strthing])
        if strthing == "trex":
            thing.Talk()
            if not thing.Hungry():
                print game.ParseText(text[strthing])
                MoveToInventory(thing)
    else:
        print game.ParseText(text["fail"])
        return
    if strthing == "troll":
        # TODO: FIND FIX FOR ANNOYING FIREFOX BUG
        webbrowser.open("http://www.youtube.com/watch?v=TancpHm4f4A")
        game.Restart()
                
def MoveToInventory(thing):
    if str(thing) not in game.Inventory():
        item = game.Vars().pop(str(thing))
        game.Inventory().append(str(thing))
        

def RemoveFromInventory(thing):
    if str(thing) in game.Inventory():
        game.Inventory().remove(str(thing))

def _checkexists(strthing):
    for item in game.Vars():
        if str(item) == strthing:
            return True
    return False