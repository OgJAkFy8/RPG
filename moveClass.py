class movement(a):
    def __init__(self, a, **keywords):
        if a == "":
            print("No empty strings")
        else:
            self.on_g()
    def on_g(self):
        print('hello there')


        
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
    match direction:
        case "L":
            print("You turn left.")
        case "R":
            print("You turn right.")
        case "B":
            print("You turn back.")
        case _:
            print("Looking around")