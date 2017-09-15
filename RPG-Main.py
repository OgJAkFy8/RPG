from random import randint
import time
#from GamePic import location
from gameMove import *

vDirection = "G"
game = "red"


## Functions 
class weapon:
    def __init__(self,name,hitpoint,magic):
        self.name = name
        self.damage = hitpoint
        self.magic = magic
        

class monster:
    def __init__(self, name, hitpoint, strngth):
        self.name = name
        self.health = hitpoint
        self.strength = strngth
        self.attacks = [] #empty list for each monster

    def add_attacktype(self, attack_type):
        self.attacks.append(attack_type)

class hero:
    def __init__(self, name, hitpoint, weapon):
        self.name = name
        self.health = hitpoint
        #self.strength = strngth
        self.weapon = [] # empty list for each weapon
        self.backpack = [] # backpack
        self.magicbag = []
        self.spell = []

    def add_weapons(self, new_weapon):
        self.weapon.append(new_weapon)

    def add_Item(self, new_item):
        self.backpack.append(new_item)

    def add_magicitem(self, new_magicitem):
        self.magicbag.append(new_magicitem)

    def add_spell(self, new_spell):
        self.spell.append(new_spell)

    def modBattle(vHeroH,vMonsterH):
        #vHeroH = Erik.health
        #vMonsterH = Troll.health

        while vHeroH > 0:
            RunFight = input("Run or Attack? [R/A] ")
            print(vHeroH)
        if RunFight == "A" or "a":
            heroAttack = randint(0,2)
            vMonsterH = vMonsterH - heroAttack
            monsterAttack = randint(0, 3)
            vHeroH = vHeroH - monsterAttack
            print("After this fight your health is at {}. the monster is at {}.".format(vHeroH, vMonsterH))


#### Dictionary Statements ######

# map the inputs to the function blocks

##options = {0 : DeadEnd(),
##           1 : Forward(),
##           2 : LeftRight(),
##           3 : ForwardLeftRight(),
##           }
##




#### START Program #####

eja = hero("Erik",9,"club")
troll = monster("Troll",10,2)


##
##if vDirection == "R":
##        print('You open the door and seen a troll')
##        RunFight = input("Run or Attack? [R/A] ").lower()
##        if RunFight == "A" or "a":
##            print(eja.health)
##            modBattle(eja.health,troll.health)
##elif vDirection == "T":
##        print('The trap door is heavy and you need to get help')
##        print(" ")
##        vHelp = input("Do you ask for help or just leave? H=Help, L=Leave: ").lower()
##        if vHelp == "H" or "h":
##            print("You ask the group for help")
##            vYesNo = randint(0,1)
##            if vYesNo == 0:
##                print(vYesNo)
##                print("Nobody wants to help")
##            else:
##                print(vYesNo)
##                print("One of your team members help")
##                vYesNo = randint(0,10)
##                if vYesNo < 5:
##                    print(vYesNo)
##                    print("You open the trap door and see a sleeping dragon")
##                else:
##                    print(vYesNo)
##                    print("You open the trap door and are eaten by the dragon inside")
##elif vDirection == "F":
##        print('You move on down the hallway')
##else:
##        exit
