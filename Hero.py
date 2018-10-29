class Hero:

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.inventory = []

    def pick_up(self, item):
        self.inventory.append(item)


def create_hero():
    name = ""
    while name == "":
            name = input("What is your name, young adventurer? > ")
    return Hero(name)
