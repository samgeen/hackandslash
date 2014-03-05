'''
Created on 5 Mar 2014

@author: samgeen
'''

import webbrowser
import Animals, Talk
game = None


text = {}
text["null"] = "I can't see that thing. Are you sure that thing exists, $PLAYERNAME? I'm not. Let's pretend you didn't do that."
text["player"] = "You climb into your inventory. It's cosy in here!"

def get(thing):
    try:
        strthing = str(thing)
    except:
        strthing = "null"
    if strthing in text:
        print game.ParseText(text[strthing])
        MoveToInventory(thing)
    if strthing == "t-rex":
        if type(thing) == type(Animals.TRex()):
            print game.ParseText(thing.Talk())
            if thing.Hungry():
                game.Restart()
            else:
                MoveToInventory(thing)
    if strthing == "troll":
        # TODO: FIND FIX FOR ANNOYING FIREFOX BUG
        webbrowser.open("http://www.youtube.com/watch?v=TancpHm4f4A")
        game.Restart()
                
def MoveToInventory(thing):
    game.Inventory().append(str(thing))
    try:
        game.Vars().remove(thing)
    except:
        pass    

