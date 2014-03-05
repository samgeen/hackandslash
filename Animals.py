'''
Created on 2 Mar 2014

@author: samgeen
'''

def MakeAnimal(name):
    if name == "llama":
        return Llama()
    if name == "t-rex":
        return TRex()

class Llama(object):
    def __init__(self):
        self._name = "llama"
        self._speech = '''The llama blinks at you. You start to describe the time you wrote a Perl script to flush your toilet.
The llama spits at you. Dribble gets all up under your hackerglasses. This is your fault, $PLAYERNAME, because you told it a very boring story and you suck.'''
        self._look = '''The llama stands unphased by the fast-moving traffic roaring past feet away. Matted white fur ripples in the slipstream.
It chews on something, though you're not sure what.'''
        
    def Look(self):
        return self._look
        
    def Name(self):
        return self._name
    
    def Talk(self):
        return self._speech
    
    def __str__(self):
        return self._name

class TRex(object):
    def __init__(self):
        self._name = "t-rex"
        self._hungry = True
        self._speechHungry = '''The t-rex eyes you with suspicion. Wait, no, that's not suspicion, that's not suspic-. 
"Burp", says the T-Rex. You did not think this through, did you $PLAYERNAME? You did not think this through at all.'''
        self._speechFull = '''You wink at the t-rex. The t-rex winks at you. Can you high-five a t-rex? TURNS OUT YOU CAN.'''
        self._look = '''The 13 foot tall carnivore stands in a side-street. '''+self._HungerText()+'''
You're unsure why there should be a t-rex here, but presumably someone put it there. Yours not to question why, you suppose.'''
        
    def Name(self):
        return self._name
    
    def Look(self):
        return self._look
    
    def Talk(self):
        if self._hungry:
            return self._speechHungry
        else:
            return self._speechFull
    
    def Hungry(self):
        return self._hungry
        
    def __str__(self):
        return self._name
        
    def _HungerText(self):
        if self._hungry:
            return "It eyes you with a hungry gaze. "
        else:
            return "It burps, its hunger sated. "
