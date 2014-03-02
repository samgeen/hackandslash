'''
Created on 2 Mar 2014

@author: samgeen
'''

class Llama(object):
    def __init__(self):
        self._name = "llama"
        self._speech = '''The llama blinks at you. You start to describe the time you wrote a Perl script to flush your toilet.
The llama spits at you. Dribble gets all up under your hackerglasses. This is your fault, $PLAYERNAME, because you told it a very boring story and you suck.'''
        
    def Name(self):
        return self._name
    
    def Talk(self):
        return self._speech
