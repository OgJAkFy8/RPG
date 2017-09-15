from random import randint
import time
#from GamePic import location
from gameMove import *

vDirection = "G"
game = "red"


while game != "exit":
    vSurrounding = ["Hallway","Door","Trapdoor"]
    print("Looking around at your surroundings you see a",vSurrounding[randint(0,2)])

    vChooseDirection = input("Choose a direction F=Forward, R=Right Door, T=Trap Door, L=leave: ")
    vDirection = vChooseDirection.upper()

    turn(vDirection)
    game = vChooseDirection
