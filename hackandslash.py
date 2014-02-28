'''
Created on Feb 28, 2014

@author: sgeen
'''

code_globals = {}

def interpret(uin):
    # Undo Python easteregg
    if "import antigravity" in uin:
        uin = "import antigrav"
    try:
        codeObj = compile(uin, "<string>", "exec")
        exec codeObj in code_globals
    except:
        print "COMMAND NOT RECOGNISED, PUNK"

def run():
    while 1:
        uin = raw_input("> ")
        interpret(uin)

if __name__=="__main__":
    run()