import Weapon as We


class Mob:

    def __init__(self, name):
        self.name = name
        if name == "Kobold":
            self. weapon = We.Weapon("Kobold Spear")
            self.maxhp = 40
            self.hp = 40

    def hp_check(self):
        if self.hp > 0.9*self.maxhp:
            print(self.name, "is looking healthy")
        elif self.hp > 0.75*self.maxhp:
            print(self.name, "is lighty wounded and showing signs of fatigue")
        elif self.hp > 0.5*self.maxhp:
            print(self.name, "is wounded, the battle has taken its toll")
        elif self.hp > 0.25*self.maxhp:
            print(self.name, "is badly wounded!")
        elif self.hp > 0.1*self.maxhp:
            print(self.name, "is bleeding profusely and seems to be on the brink of death.")
