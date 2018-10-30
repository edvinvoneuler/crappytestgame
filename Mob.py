import Weapon as We


class Mob:

    def __init__(self, name):
        self.name = name
        if name == "Kobold":
            self. weapon = We.Weapon("Kobold Spear")
            self.hp = 40
