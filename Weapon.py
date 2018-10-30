import random


class Weapon:

    def __init__(self, name):
        self.name = name

        if name == "Sword":
            self.dmg = range(35, 41)
            self.cth = 0.75  # chance to hit

        elif name == "Fists":
            self.dmg = range(5, 6)
            self.cth = 0.8

        elif name == "Spear":
            self.dmg = range(22, 27)
            self.cth = 0.95

        elif name == "Dagger":
            self.dmg = range(10, 16)
            self.cth = 0.80

        elif name == "Claws":
            self.dmg = range(10, 12)
            self.cth = 0.7

        elif name == "Bite":
            self.dmg = 18
            self.cth = 0.4

        elif name == "Kobold Spear":
            self.dmg = range(8, 9)
            self.cth = 0.6

    def strike(self):
        if random.uniform(0, 1) > self.cth:
            print('The attack missed!')
            return 0
        else:
            print('The attack struck true!')
            return self.dmg[random.randint(0, len(self.dmg))-1]


# test_sword = Weapon("Sword")
#
# for i in range(0, 5):
#     print(test_sword.strike())
