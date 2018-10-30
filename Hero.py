import Mob
import Weapon as We
import random


class Hero:

    def __init__(self, name):
        self.name = name
        self.hp = 100
        fists = We.Weapon("Fists")
        self.inventory = [fists, ]

    def pick_up(self, item):
        self.inventory.append(item)

    def get_item_from_name(self, name):
        for item in self.inventory:
            if item.name == name:
                return item

    def fight(self, mob):

        choice = None
        print('You have:')
        for item in self.inventory:
            print(item.name)
        print('in your inventory.')
        while choice not in [item.name for item in self.inventory]:
            choice = input("which weapon do you choose? >")
        weapon = self.get_item_from_name(choice)

        while self.hp > 0:
            mob.hp = mob.hp - weapon.strike()
            if mob.hp > 0:
                self.hp = self.hp - mob.weapon.strike()
        print("The", mob.name, "is defeated.")


def create_hero(name=""):
    name = name
    while name == "":
        name = input("What is your name, young adventurer? > ")
    return Hero(name)


you = create_hero("ASSFACE")

sword = We.Weapon("Sword")

you.pick_up(sword)

for item in you.inventory:
    print(item.name)

mob = Mob.Mob("Kobold")
you.fight(mob)
