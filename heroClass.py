class Hero:
    hp = 2  # Hit Points
    sl = 5  # Skill Level
    ap = 5  # Attack Power

    def __init__(self, name):
        self.name = name
        self.attack = []  # creates a new empty list for each Monster
        self.magicStore = []

    def add_attack(self, attack):
        self.attack.append(attack)
        # magic = self.attack.copy()

    def magic_attack(self, attack):
        self.attack.remove(attack)

    def mspell(self, jspell):
        # if jspell == "save":
        Store = self.attack.copy()
        # else jspell == "restore":
        # self.attack(Store)
        return Store

    def jspell(self, jspell):
        # if jspell == "save":
        # Store = self.attack.copy()
        # else jspell == "restore":
        self.attack(Store)
        return Store


class Spell:

    def __init__(self, name, method):
        self.name = name
        self.method = method
        self.magicStore = []


class Foo(object):
    def __init__(self, q, **keywords):
        if q == "":
            print("No empty strings")
        else:
            self.on_g()

    def on_g(self):
        print('hello there')


class Weapon:
    magic = 0  # Set to 1 if magic
    kind = ""

    # if kind = "Magic"
    hp = 5  # Hit Points. The amount of rounds it can be used
    sl = 1  # Skill Level.  The amount of skill needed to use this weapon
    ap = 1  # Attack Power. The damage it can do in one use

    def __init__(self, name):
        self.name = name


class Holder:
    magic = 0  # Set to 1 if magic

    kind = "bag"  # What it is.  backpack, trunk, pouch
    sz = 1  # Size - In pounds

    def __init__(self, name):
        self.name = name
        self.item = []

    def add_item(self, item):
        self.item.append(item)
