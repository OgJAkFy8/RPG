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
        result = randint(0,1)
        if cointype == "wooden":
            result = mc
        if int(result) == 0:
            print("Flip #{0} is heads.".format(i+1))
        else:
            print("Flip #{0} is tails.".format(i+1))
# ----------------------------
# Dice Rolling
def rolldice(sides=6,times=1,dicetype='ivory'):
    rollTotal = 0

    if dicetype == "magic":
        mr = input("Number to roll [1-{0}] : ".format(sides))
        magicresult = int(mr)
        
    for i in range(times):
        time.sleep(.33)

        if dicetype == "magic":
            result = magicresult
            print("Rolling the wooden die.")
        else:
             result = randint(1,sides)
             print("Rolling the {} die.".format(dicetype),end="\n")
            
        rollTotal = rollTotal + result
        if times < 7:
            print("Roll #{} is a {}.".format(i+1,result))
        elif times <= 16:
            print("R#{0} = {1}".format(i+1,result), end=" | ")
        else:
            print("R#{0} = {1}".format(i+1,result),end=" | ")
            
#    print()
    print("The total of all your rolls: {0}.".format(rollTotal),end="\n")


