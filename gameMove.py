# To make people or monsters move

#Import Modules

#Define Variables
vDirection = "G"



def walk(weight,energy):
        distance = (energy)*(weight/4)
        print("you covered ", distance," meters")

def run(weight, energy):
    if energy > 5:
        energy = 5
    if energy == 1:
        print("You don't have enough energy to run and have to walk.")
        energy = 0
    elif energy == 0:
        print("You have to rest.")
    else:
        distance = (energy)*(weight/4)
        print("you covered ", distance," meters")
        energy = 1
    
def turn(direction):
    if direction == "L":
        print("You turn left.")
    elif direction == "R":
        print("You turn right.")
    elif direction == "B":
        print("You turn back.")
    else:
        print("Looking around")
    
        
    pass

def attack():
    pass

##
##
##while vDirection != "L":
##    print("You are standing in a space.")
##    #location("hall")
##    #GamePic.py
##    l_Direction = ["F","R","L","B","T","L"]
##
##    vDirection = (input("Choose a direction F=Forward, R=Right Door, T=Trap Door, L-leave: ")).upper()
##
##    if vDirection in l_Direction:
##        if vDirection == "R":
##            print('You open the door and seen a troll')
##        elif vDirection == "T":
##            print('The trap door is heavy and you need to get help')
##        elif vDirection == "F":
##            
##            print('You move on down the hallway')
##        else:
##           # vDirection == "L":
##            print('Good bye')
##            exit
##    else:
##        print('You did not select anything correctly. And in this case not making a choice just stops the program.')
##        vDirection = ""
##exit
