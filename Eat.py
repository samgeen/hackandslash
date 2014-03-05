'''
Created on 5 Mar 2014

@author: samgeen
'''

game = None

text = {}
text["haxsnax"] = "Mmm, haxsnax! They're cyberlicious!"
text["sword"] = '''As all of your organs are perforated and blood begins pooling in places it shouldn't, your last thought before blacking out is
"I should have thought this one through more carefully."'''
text["llama"] = '''You are hungry. So hungry you could eat a llama. So you do. Monster.'''
text["t-rex"] = '''You were really hungry! Still, that t-rex filled a hole. A hole that is now tearing itself in your abdomen, 
as an enraged prehistoric carnivore rips its way out of your stomach. You really should have thought that one through.'''
text["cyberogres"] = '''You, uh... I guess you can eat the cyberogres. Huh. I didn't think, but I guess it says here... well OK then.'''
text["null"] = "You can't eat that, $PLAYERNAME"
text["player"] = "Uh, you want to eat... right, OK then. You eat yourself and you die. Well done, you."

deadly = ["sword", "t-rex", "player"]
win = ["cyberogres"]

def eat(thing):
    strthing = str(thing)
    if not strthing in game.Inventory():
        print game.ParseText('''If it's not in your inventory you can't eat it! What are you gonna do, 
scarf it off the floor, $PLAYERNAME? For serious.''')
        return
    print game.ParseText(text[strthing])
    if strthing in deadly:
        game.Restart()
    if strthing in win:
        game.Win()