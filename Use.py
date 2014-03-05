'''
Created on 5 Mar 2014

@author: samgeen
'''

import sys
import Get

game = None

def use(thinga, thingb):
    stra = str(thinga)
    strb = str(thingb)
    if stra == strb:
        print game.ParseText("You think you're being clever, $PLAYERNAME, but you're not.")
        return
    if not stra in game.Inventory():
        print game.ParseText("Yo, $PLAYERNAME, that's not in your inventory. Soz and all that.")
        return
    if not thingb in game.Vars() or strb in game.Inventory():
        print game.ParseText("Yeah, that's not a thing that exists either in the world or in your inventory. So, no.")
        return
    if stra == "sword":
        if strb == "cyberogres":
            if "llama" in game.Inventory():
                print game.ParseText('''You mount the llama. Your mighty steed charges the cyberogres, 
killing one with a blow from its hooves. You slay the second with a slash of your cybersword. You are victorious!''')
                game.Win()
            elif "t-rex" in game.Inventory():
                print game.ParseText('''You mount the t-rex and raise your sword towards you foes. 
It charges them down, swallowing them both with a mighty gulp. You are victorious!''')
                game.Win()
            else:
                print game.ParseText('''You brandish your cybersword. The cyberogres pop into a fighting stance.
You slash at the first cyberogre, slaying them with a mighty blow. The second one comes up behind you and 
crushes your skull. You needed that skull! Man.''')
                game.Restart()
            return
        if strb == "player":
            print game.ParseText("Uh, you stab yourself. OK.")
            game.Restart()
        if strb == "llama":
            print game.ParseText('''Why would you... uh, whatever. You stab the llama and it dies. Monster.''')
            Get.RemoveFromInventory(thingb)
            return
        if strb == "t-rex":
            print game.ParseText('''You brandish the sword at the t-rex. The t-rex is having none of that and eats you.''')
            game.Restart()
    if stra == "llama":
        if strb == "cyberogres":
            modstr = "Shame you don't have a module called Animals imported so you can just spawn another one hint hint."
            if "Animals" in sys.modules.keys():
                print "Lucky you can just make another one in the Animals module, right?"
            print game.ParseText('''The cyberogres rip the llama in two. "LLAAAAAMAAAAAA!" you cry, distraught. '''+modstr)
            return
        if strb == "sword":
            print game.ParseText('''The llama looks at the sword, but doesn't quite understand how that might work.''')
            return
        if strb == "t-rex":
            print game.ParseText('''The t-rex eats the llama. Monster.''')
            Get.RemoveFromInventory(thinga)
            return
        if strb == "player":
            print game.ParseText('''The llama licks you. Ew. Ew.''')
            return
        if strb == "haxsnax":
            print game.ParseText('''The llama eats the haxsnax. Yum.''')
            Get.RemoveFromInventory(thingb)
            return
    if stra == "cyberogres":
        if strb == "player":
            print game.ParseText('''The cyberogres are angry at being trapped in your inventory and murder you. So.''')
            game.Restart()
        if strb == "haxsnax":
            print "The cyberogres eat your haxsnax! Oh no!"
            Get.RemoveFromInventory(thingb)
            return
        if strb == "sword":
            print game.ParseText("So you decide to give two dangerous cyberogres your only weapon. Whatever, it's your adventure.")
            Get.RemoveFromInventory(thingb)
            return
    if stra == "t-rex":
        if strb == "llama":
            use(thingb, thinga)
            return
        if strb == "haxsnax":
            print game.ParseText("The t-rex chomps down the haxsnax. It is hungry no more! Success. Cybersuccess.")
            Get.RemoveFromInventory(thingb)
            thinga.Hungry(False)
            return
        if strb == "sword":
            print game.ParseText("The t-rex's arms are too small to use the sword. Alas.")
            return
        if strb == "cyberogres":
            print game.ParseText("The t-rex eats the cyberogres. This is incredibly grizzly to watch, but, uh, victory, I guess?")
            game.Win()
    if stra == "haxsnax":
        if strb == "llama" or strb == "t-rex" or strb == "cyberogres":
            use(thingb, thinga)
            return
        if strb == "player":
            print game.ParseText('''Cyberlicious! You eat the haxsnax.''')
            Get.RemoveFromInventory(thingb)
            return
    if stra == "player":
        use(thingb, thinga)
        return
    
    # Default failure text
    game.ParseText('''You know what, I can't be bothered to make up an interaction between those things, so no, you can't do that.''')
