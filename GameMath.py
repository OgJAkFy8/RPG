# This module is to be used for in game calculation to reduce the size
# of the program

# The dice roll
def diceroll(d_side,rolls):
    import random, time
    x=0
    j=0
    results = [0]
    print("Rolling the",d_side,"sided dice",rolls,"times")
    while x < rolls:
        x=x+1
        results.append(random.randint(1,d_side))
        print("Roll #",x,' is ',results[x])
        j=.125+.125
        time.sleep(j)
    s = sum(results)
    print("The total of all rolls is",s)


# The coin flip
def coinflip(times,cheat=".",magic="."):
    import random, time
    j=.125
    x=0
    h=2
    t=1
    results = [0]
    print("Flipping the coin",times,"times.")
    while x < times:
        x=x+1
        if cheat == "h" or "H":
            h = 1
        elif cheat == "t" or "T":
            t = 2
        else:
            t = 1
            h = 2
        fresult = random.randint(t,h)   
        if fresult == 2:
            side = "Tails"
        else:
            side = "Heads"
        #results.append(fresult)
        print("Flip #",x," is", side)
        time.sleep(j)      



