'''
Created on 2 Mar 2014

@author: samgeen
'''

class Level(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self._name = name
        self._text = ""
        self._look = ""
        self._death = ""
        
    def Name(self):
        return self._name
        
    def Text(self):
        return self._text
    
    def Look(self):
        return self._look
    
    def Death(self):
        return self._death