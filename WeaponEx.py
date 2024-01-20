class Weapon:
    magic = 0  # Set to 1 if magic
    kind = ""

    # if kind = "Magic"
    hp = 5  # Hit Points. The damage it can do in one use
    sl = 1  # Skill Level.  The amount of skill needed to use this weapon
    ad = 1  # Attack Duration. The amount of rounds it can be used

    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

    def __str__(self):
        return f"{self.name}({self.hp})"

    def normalattack(self):
        y = self.hp * self.level
        return y


A1 = Weapon('axe', 5, 2)
print(A1)
print(A1.normalattack())
