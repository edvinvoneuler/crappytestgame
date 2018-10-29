class Weapon:

    def __init__(self, name):
        self.name = name
        if name == "Sword":
            self.dmg = range(35, 41)
            self.cth = 0.75  # chance to hit

        elif name == "Spear":
            self.dmg = range(22, 27)
            self.cth = 0.95

        elif name == "Dagger":
            self.dmg = range(10, 16)
            self.cth = 0.80
