'''
Created on 2 Mar 2014

@author: samgeen
'''
import Animals

class Player(object):
    def __init__(self):
        self._name = "punk"
        
    def Name(self, newname=None):
        '''
        If newname is not None, set the Player's name to newname
        Return: player's name
        '''
        if not newname is None:
            self._name = newname
        return self._name
    
    def __str__(self):
        return "player"
    
animalname = "llama"

cmdvars = {"punk": Player(),
           "animalname": animalname,
           "level": None,
           "inventory": []}