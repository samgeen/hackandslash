'''
Created on 5 Mar 2014

@author: samgeen
'''

game = None

talkmute = "This thing can't talk. Or maybe it can, but doesn't want to. Either way."

def talk(thing):
    try:
        thing.Talk()
    except:
        print game.ParseText(talkmute)