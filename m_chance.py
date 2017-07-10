from random import randint
import time


## Functions -----------
# Coin Flip
def coin(flips=1,cointype="silver"):
    if cointype == "magic":
        mc = input("Would you like heads [0] or tails [1]?")
        cointype = "wooden"
    print("Flipping a {0} coin".format(cointype))
    for i in range(flips):
        time.sleep(.33)
        if cointype != "wooden":
            result = randint(0,1)
        else:
            result = mc
        if int(result) == 0:
            print("Flip {0} is heads.".format(i+1))
        else:
            print("Flip {0} is tails.".format(i+1))
# ----------------------------
# Dice Rolling
def rolldice(sides,times=1,dicetype='ivory'):
    rollTotal = 0
    print("Rolling the {} die.".format(dicetype),end="\n")
    for i in range(times):
        time.sleep(.33)
        result = randint(1,sides)
        rollTotal = rollTotal + result
        if times <= 7 or dicetype=="magic":
            print("Roll #{} is a {}.".format(i+1,result))
        elif times <= 16:
            print("#{0} = {1}".format(i+1,result), end=" | ")
        else:
            print("{0}={1}".format(i+1,result),end=" | ")
            
    print()
    print("The total of all your rolls: {0}.".format(rollTotal))


