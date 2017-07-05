from random import randint
import time
from GamePic import location

vDirection = "G"


## Functions 
def rolldice(sides):
    if sides == 2:
        print("Flipping gold coin")
        result = randint(0,sides)
    elif sides == 4:
        while i > 20:
            result = randint(1,sides)
            print(result)
    elif sides == 6:
        while i > 20:
            result = randint(1,sides)
            print(result)
    elif sides == 8:
        while i > 20:
            result = randint(1,sides)
            print(result)
    elif sides == 10:
        while i > 20:
            result = randint(1,sides)
            print(result)
    elif sides == 20:
        while i > 20:
            result = randint(1,sides)
            print(result)
            i= i-1
            j=.125+.125
            time.sleep(j)
    elif sides == 100:
        while i > 20:
            result = randint(1,sides)
            print(result)
    else:
        print("____________")
    return result

class weapon:
    def __init__(self,name,hitpoint,magic):
        self.name = name
        self.damage = hitpoint
        self.magic = magic

        #def add_

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

while vDirection != "L":
    print("You are standing in a space.")
    location("hall")
    #GamePic.py
    vChooseDirection = input("Choose a direction F=Forward, R=Right Door, T=Trap Door, L-leave: ")
    vDirection = vChooseDirection.upper()
    if vDirection == "R":
        print('You open the door and seen a troll')
        RunFight = input("Run or Attack? [R/A] ").lower()
        if RunFight == "A" or "a":
            print(eja.health)
            modBattle(eja.health,troll.health)
        elif vDirection == "T":
            print('The trap door is heavy and you need to get help')
            print(" ")
            vHelp = input("Do you ask for help or just leave? H=Help, L=Leave: ").lower()
            if vHelp == "H" or "h":
                print("You ask the group for help")
                vYesNo = randint(0,1)
            if vYesNo == 0:
                print(vYesNo)
                print("Nobody wants to help")
            else:
                print(vYesNo)
                print("One of your team members help")
                vYesNo = randint(0,10)
                if vYesNo < 5:
                    print(vYesNo)
                    print("You open the trap door and see a sleeping dragon")
                else:
                    print(vYesNo)
                    print("You open the trap door and are eaten by the dragon inside")
    elif vDirection == "F":
        print('You move on down the hallway')
    else:
        print('You did not select anything correctly. And in this case not making a choice just stops the program.')
        vDirection = ""
        print('Good bye')
exit