from random import randint

class Weapon:
    hp = 5  # Hit Points. The damage it can do in one use
    sl = 1  # Skill Level.  The amount of skill needed to use this weapon
    ad = 1  # Attack Duration. The amount of rounds it can be used

    def __init__(self, name, hp, charlevel,magic  ):
        self.name = str(name)
        self.hp = int(hp)
        self.charlevel = int(charlevel)
        self.__magic  = bool(magic)

    def __str__(self):
        if self.charlevel > 4:
            return f"{self.name}(hp = {self.hp}*)"
        else:
            return f"{self.name}(hp = {self.hp})"


    def normalattack(self):
        y = randint(0,self.hp)

        if self.__magic == True and self.charlevel > 4:
            y = y + self.hp
        return y




sling = Weapon('sling', 4,2,False)
sling1 = Weapon('sling1',3,2,True)  # Magic sling with charlevel not high enough to use it.
sling2 = Weapon('sling2',3,5,True)  # Magic sling with charlevel high enough to use it.

print(sling)
print(sling.normalattack())
print(sling1)
print(sling1.normalattack())
print(sling2)
print(sling2.normalattack())
