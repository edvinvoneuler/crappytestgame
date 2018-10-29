class Room:

    def __init__(self, desc, left=None, right=None, straight=None, path=None):
        self.desc = desc
        self.left = left
        self.right = right
        self.straight = straight
        self.path = path
        self.back = None

    def enter(self):
        print(self.desc)
        if "died" in self.desc:
            print('You have Lost!')
        elif "you won!" in self.desc:
            print('Congratulations, you won!')
        else:
            print("The following paths lead out of this room:")
            if self.left is not None:
                print('\nleft:')
                print(self.left.path)
            if self.straight is not None:
                print('\nstraight:')
                print(self.straight.path)
            if self.right is not None:
                print('\nright:')
                print(self.right.path)

            self.exit()

    def exit(self):
        answer = ""
        while answer not in ["left", "right", "straight"]:
            answer = input("\nWhere do you want to go?").lower()
        if answer == "left":
            self.left.enter()
        elif answer == "right":
            self.right.enter()
        elif answer == "straight":
            self.straight.enter()

