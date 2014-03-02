'''
Created on Mar 1, 2014

@author: sgeen
'''

import LevelData, Verbs, Animals
import os, copy, readline, textwrap, time

debug = False

class Player(object):
    def __init__(self):
        self._name = "punk"
        
    def Name(self):
        return self._name

speech = r"'''"
titletext = '''
HACK AND SLASH: An Adventure in Cybercity
Created on Mar 01, 2014
@author: Sam Geen
@generator: python2.7
'''
titletext = speech+titletext+speech
coolanimal = Animals.Llama()

cmdvars = {"punk": Player(),
           "coolanimal": coolanimal,
           "level": None}

parsevars = {"$PLAYERNAME": "punk.Name()",
            "$COOLANIMAL": "coolanimal.Name()"}

class Game(object):
    '''
    Main game object
    '''
    def __init__(self):
        self._cmdvars = None
        self._parsevars = None
        self._verbs = None

    def Start(self):
        print titletext
        self.Restart(dead=False)
        while 1:
            uin = raw_input("> ")
            readline.write_history_file("cmdhistory.dat")
            self.Interpret(uin)
            
    def Restart(self, dead=True):
        '''
        Restart the game
        TODO: MAKE THIS WORK BETTER
        '''
        if dead:
            print "\nYou,", str(self._cmdvars["punk"].Name())+", are cyberdead. Let's try that one again."
            time.sleep(2.0)
            print "------------"
        self._cmdvars = cmdvars
        self._parsevars = parsevars
        self._verbs = Verbs.Verbs(self)
        cmdvars["verbs"] = self._verbs
        self.ChangeLevel(LevelData.intro)
        
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
        verbs = dir(self._verbs)
        itemised = filter(None, uin.split(" "))
        first = itemised[0]
        if first in verbs:
            newcmd = "verbs."+itemised[0]+"(punk"
            # Add rest of arguments as single string
            if len(itemised) > 1:
                newcmd += ","+" ".join(itemised[1:len(itemised)])
            newcmd += ")"
            # Run new argument
            codeObj = compile(newcmd, "<string>", "exec")
            exec codeObj in self._cmdvars
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
                exec codeObj in self._cmdvars
        except:
            print "Input failed,", self._cmdvars["punk"].Name()
            if debug:
                print self._cmdvars.keys()

def run():
    if os.path.exists("cmdhistory.dat"):
        readline.read_history_file("cmdhistory.dat")
    game = Game()
    game.Start()

if __name__=="__main__":
    run()