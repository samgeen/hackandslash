'''
Created on Mar 1, 2014

@author: sgeen
'''

import os, copy, readline, textwrap, time, inspect
import LevelData, Verbs

from CmdVars import cmdvars

debug = False


speech = r"'''"
titletext = '''
HACK AND SLASH: An Adventure in Cybercity
Created on Mar 01, 2014
@author: Sam Geen
@generator: python2.7
'''

titletext = speech+titletext+speech

parsevars = {"$PLAYERNAME": "punk.Name()",
            "$ANIMALNAME": "str(animalname)"}

class Game(object):
    '''
    Main game object
    '''
    def __init__(self):
        self._cmdvars = None
        self._parsevars = None

    def Start(self):
        Verbs.game = self
        print titletext
        self.Restart(dead=False)
        while 1:
            uin = raw_input("> ")
            readline.write_history_file("cmdhistory.dat")
            self.Interpret(uin)
            
    def Restart(self, dead=True):
        '''
        Restart the game
        TODO: MAKE THIS WORK BETTER RE: OBJECT RELOADING, ETC
        '''
        if dead:
            print "\nYou,", str(self._cmdvars["punk"].Name())+", are cyberdead. Let's try that one again."
            time.sleep(2.0)
            print "------------"
        self._cmdvars = cmdvars
        codeObj = compile("from Verbs import "+self._VerbList(), "<string>", "exec")
        exec codeObj in self._cmdvars
        self._parsevars = parsevars
        self.ChangeLevel(LevelData.intro)
        
    def _VerbList(self):
        funcs = inspect.getmembers(Verbs, inspect.isfunction)
        names = list()
        for func, pointer in funcs:
            names.append(func)
        return ", ".join(names)
        
    def Level(self):
        return self._cmdvars["level"]
    
    def ChangeLevel(self, newLevel):
        '''
        Change the current level
        '''
        self._cmdvars["level"] = newLevel
        print self.ParseText(self._cmdvars["level"].Text())
        
    def ParseText(self, text):
        newtext = copy.copy(text)
        for key, val in self._parsevars.iteritems():
            insert = eval(val, self._cmdvars)
            if debug:
                print key, insert
            newtext = newtext.replace(key, insert)
        newtext = newtext.replace("\n"," ")
        newtext = newtext.replace("  "," ")
        newtext = "\n".join(textwrap.wrap(newtext))
        return newtext

    def ParseVerb(self, uin):
        # Check for null string
        if len(uin) == 0:
            return True
        verbs = dir(Verbs)
        itemised = filter(None, uin.split(" "))
        first = itemised[0]
        if first in verbs:
            run = uin
            try:
                if uin.replace(" ","")[len(first)] == "(":
                    pass
            except:
                run = "print "+first
            codeObj = compile(run, "<string>", "exec")
            exec codeObj in self._cmdvars, self._cmdvars
            return True
        else:
            return False
    
    def Interpret(self, uin):
        # Undo Python easteregg
        #if "import antigravity" in uin:
        #    uin = "import antigrav"
        try:
            if not self.ParseVerb(uin):
                codeObj = compile(uin, "<string>", "exec")
                exec codeObj in self._cmdvars, self._cmdvars
        except:
            print "Input failed,", self._cmdvars["punk"].Name()
            if debug:
                print self._cmdvars.keys()
                raise

def run():
    if os.path.exists("cmdhistory.dat"):
        readline.read_history_file("cmdhistory.dat")
    game = Game()
    game.Start()

if __name__=="__main__":
    run()