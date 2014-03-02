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
        
    def Name(self):
        return self._name
    
    def Talk(self):
        return self._speech

class TRex(object):
    def __init__(self):
        self._name = "t-rex"
        self._speechNT = '''The t-rex eyes you with suspicion. Wait, no, that's not suspicion, that's not suspic-. "Burp", says the T-Rex. You did not think this through, 
did you $PLAYERNAME? You did not think this through at all.'''
        self._speechT = '''You wink at the t-rex. The t-rex winks at you. Can you high-five a t-rex? TURNS OUT YOU CAN.'''
        self._trust = False
        
    def Name(self):
        return self._name
    
    def Talk(self):
        if self._trust:
            return self._speechT
        else:
            return self._speechNT
