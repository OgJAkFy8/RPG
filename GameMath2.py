# This module is to be used for in game calculation to reduce the size
# of the program

# The dice roll
def diceroll(d_side,rolls):
    import random, time
    #x=0
    j=0
    results = [random.randint(1,d_side) for x in range(rolls)]
    #results = [0]
    print("Rolling the",d_side,"sided dice",rolls,"times")
    for x in range(rolls):
        #x=x+1
        #results.append(random.randint(1,d_side))
        y=x+1
        print("Roll #",y,' is ',results[x])
        j=.125+.125
        time.sleep(j)
    s = sum(results)
    print("The total of all rolls is",s)


# The coin flip
def coinflip(times,cheat=".",magic="."):
    import random, time
    x=0
    j=.25
    results = [0]
    print(cheat)
    #num = input('Number of times to flip coin: ')
    #flips = [random.randint(0,1) for r in range(times)]

    print("Flipping the coin",times,"times.")
    #flips= ['Heads' if x==1 else 'Tails' for x in [random.randint(0,1) for x in range(times)]]

    if cheat != ".":
        for x in range(times):
            if cheat == "h" or "H":
                side = "Heads"
            else:
                side = "Tails"
            y=x+1
            print("Flip #",y," is", side)
            time.sleep(j)
    else:
        for x in range(times):
            flpresult = random.randint(0,1)

            if flpresult == 0:
                side = "Heads"
            else:
                side = "Tails"
            y=x+1
            print("Flip #",y," is", side)
            time.sleep(j)
                



