import Mob
import Hero
class Room:

    def __init__(self, desc, left=None, right=None, straight=None, path=None, mob=None):
        self.desc = desc
        self.left = left
        self.right = right
        self.straight = straight
        self.path = path
        self.back = []
        self.mob = mob

    def enter(self, hero):
        print(self.desc)
        if "died" in self.desc:
            print('You have Lost!')
        elif "you won!" in self.desc:
            print('Congratulations, you won!')
        else:
            if self.mob is not None:
                print("A hostile", self.mob.name, "has appeared!")
                choice = " "
                while choice not in "YNyn":
                    choice = input("Do you want to fight it? (y/n)")
                if choice in "Nn":
                    self.back.pop().enter(hero)
                else:
                    hero.fight(self.mob)
            print("The following paths lead out of this room:")
            if self.left is not None:
                print('\nLeft:')
                print(self.left.path)
            if self.straight is not None:
                print('\nStraight:')
                print(self.straight.path)
            if self.right is not None:
                print('\nRight:')
                print(self.right.path)
            print("\nOr go back")
            self.exit(hero)

    def exit(self, hero):
        answer = ""
        while answer not in ["left", "right", "straight", "back"]:
            answer = input("\nWhere do you want to go? > ").lower()

        if answer == "left":
            self.back.append(self)
            self.left.back = self.back
            self.left.enter(hero)

        elif answer == "right":
            self.back.append(self)
            self.right.back = [] + self.back
            self.right.enter(hero)

        elif answer == "straight":
            self.back.append(self)
            self.straight.back = [] + self.back
            self.straight.enter(hero)

        elif answer == "back":
            if self.back == []:
                print("You can't go back, the entrance is locked.")
                self.exit(hero)
            else:
                self.back.pop().enter(hero)

if __name__ == "__main__":

    you = Hero.create_hero("ASSFACE")
    room_01 = Room("This room seems empty", mob=Mob.Mob("Kobold"))
    room_01.enter(you)

