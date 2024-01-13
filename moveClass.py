
def turn(direction):
    match direction:
        case "L":
            print("You turn left.")
        case "R":
            print("You turn right.")
        case "B":
            print("You turn back.")
        case _:
            print("Looking around")

turn("L")