import Mob
import Weapon as We
import random
import sys
import time


class Hero:

    def __init__(self, name):
        self.name = name
        self.maxhp = 100
        self.hp = 100
        fists = We.Weapon("Fists")
        self.inventory = [fists, ]

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
            print('You attack your foe:')
            time.sleep(1)
            mob.hp = mob.hp - weapon.strike()
            time.sleep(1)
            mob.hp_check()
            if mob.hp > 0:
                time.sleep(1)
                print(mob.name, 'is attacking you:')
                time.sleep(1)
                self.hp = self.hp - mob.weapon.strike()
                time.sleep(1)
                self.hp_check()
                time.sleep(1)

            else:
                break
        if self.hp < 0:
            print('You\'ve been defeated by a', mob.name, "\n You are dead.")
            sys.exit()
        time.sleep(1)
        print("The", mob.name, "is defeated!")


def create_hero(name=""):
    name = name
    while name == "":
        name = input("What is your name, young adventurer? > ")
    return Hero(name)


if __name__ == "__main__":
    you = create_hero("ASSFACE")

    sword = We.Weapon("Sword")

    you.pick_up(sword)

    mob = Mob.Mob("Kobold")
    you.fight(mob)
