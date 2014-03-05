'''
Level info storage

Created on 2 Mar 2014

@author: samgeen
'''

import Animals
from Level import Level

# LEVELS

intro = Level("intro") 
intro._text = '''You are standing atop a cybertower. The cityscape is a swimming mirage of 
hot pinks and ice-slick blues. Sirens wail, a dark, dense forest of 
screaming sine functions. You watch as two cyberogres leap into the 
bit-choked streets below. The air smells faintly of antifreeze, thermal 
paste and $ANIMALNAME piss.

Just another day for you, $PLAYERNAME, in Cybercity.
'''
intro._look = '''The mean streets of Cybercity swim below, glistening rain-flecked cars rushing in either direction, 
traffic appearing and disappearing like ones and zeroes in the bitstream, insert serial bus joke. On the other side of the street, hackers hang out by the neon-lit "Import-Export",
hacking fingers itchy from underuse, ready for a fight. Just another day in Cybercity. Except it looks like it's night because cyberpunk.'''
intro._death = '''A cyberpigeon craps on you, rancid droppings seeping into a cut inflicted by the barber as they shaved your cool cyber-do. 
Weeks later, in hospital, you succumb to the bit rot.'''
def introsetup(game):
    vars = game.Vars()
    vars["inventory"] = ["sword", "haxsnax"]
    if "trex" in vars:
        vars.pop("trex")
    if "cyberogres" in vars:
        vars.pop("cyberogres")
    if "llama" in vars:
        vars.pop("llama")
intro.Setup = introsetup

# -------------------------------------------------- #


streets = Level("streets")
streets._text = '''You land on the mean streets of Cybercity. Cars rush past, glittering like rain-flecked pearls in the neon streetlamps, 
even though it's like noon, because this is cyberpunk and actual sunlight is illegal or something. There are two cyberogres in front of you, 
having patiently observed you as you glide to the ground. A feral $ANIMALNAME stares at the scene from an alleyway.'''
streets._look = '''The cyberogres look mean! Better hope you have a weapon, $PLAYERNAME, or you're bit-toast.'''
streets._death = '''You see a bitcoin on the street and bend down to pick it up. You are killed by a combination of crippling deflation, 
wild value fluctuations and the fevered masturbation fantasies of people who live in the mountains and hide gold under their mattresses.'''
def streetssetup(game):
    game.Vars()["cyberogres"] = Animals.MakeAnimal("cyberogres")
    animalname = game.Vars()["animalname"]
    game.Vars()[animalname] = Animals.MakeAnimal(animalname)
streets.Setup = streetssetup