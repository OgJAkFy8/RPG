# This module is to be used for in game calculations

# Import modules for use in the program
import random, time


# The dice roll
def diceroll(d_side,rolls):
    j=0
    results = [random.randint(1,d_side) for x in range(rolls)]
    print("Rolling the",d_side,"sided dice",rolls,"times")
    for x in range(rolls):
        y=x+1
        print("Roll #",y,' is ',results[x])
        j=.125+.125
        time.sleep(j)
    s = sum(results)
    print("The total of all rolls is",s)


# The coin flip
def coinflip(times,cheat="."):
    x=0
    j=.25
    results = [0]
    
    print("Flipping the coin",times,"times.")

    for x in range(times):
        fresult = random.randint(0,1)
        if cheat != ".":
            fresult = cheat

        if fresult == 0:
            side = "Heads"
        else:
            side = "Tails"

        y=x+1
        print("Flip #",y," is", side)
        time.sleep(j)
