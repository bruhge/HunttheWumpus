import random


class WumpusGame(object):
    def __init__(self):
        cave = {1: (2, 5, 8),
                2: (1, 3, 10),
                3: (2, 4, 12),
                4: (3, 5, 14),
                5: (1, 4, 6),
                6: (5, 7, 15),
                7: (6, 8, 17),
                8: (1, 7, 11),
                9: (10, 12, 19,),
                10: (2, 9, 11),
                11: (8, 10, 20),
                12: (3, 9, 13),
                13: (12, 14, 18),
                14: (4, 13, 15),
                15: (6, 14, 16),
                16: (15, 17, 18),
                17: (7, 16, 20),
                18: (13, 16, 19),
                19: (9, 18, 20),
                20: (11, 17, 19)}

        self.cave = cave
        self.threats = {}
        self.arrows = 5
        self.playerPos = 0

    def safe_rooms(self):
        return list(set(self.cave.keys()).difference(self.threats.keys()))

    def set_cave(self):
        threat_list = ['bat', 'bat', 'pit', 'pit', 'wumpus']

        for threat in threat_list:
            room = random.choice(self.safe_rooms())
            self.threats[room] = threat

        self.playerPos = random.choice(self.safe_rooms())

    def print_warning(self):
        for value in self.cave[self.playerPos]:
            if self.threats.get(value) == 'bat':
                print("You hear a rustling")
            elif self.threats.get(value) == 'pit':
                print("You feel a cold wind blowing from a nearby cavern")
            elif self.threats.get(value) == 'wumpus':
                print("You smell something terrible nearby.")

    def gameOver(self, value):
        if self.threats.get(value) == 'pit':
            print('You fell in a pit.  Game over')
            return 0
        elif self.threats.get(value) == 'wumpus':
            print('You were eaten by the wumpus.  Game over')
            return 0
        elif self.threats.get(value) == 'bat':
            self.playerPos = random.choice(self.safe_rooms())
            return 1
        return 1

    def move(self, value):
        if value in self.cave[self.playerPos]:
            self.playerPos = value
        else:
            print("You cannot move here")

    def shoot(self, value):
        if value in self.cave[self.playerPos]:
            if self.threats.get(value) == 'wumpus':
                print("Congrats you win")
                return 0
            self.arrows -= 1
            if self.arrows < 1:
                print("You are out of arrows and the game is over")
                return 0
            return 1

    def gamePlay(self):
        self.set_cave()
        keepGoing = 1
        while keepGoing > 0:
            self.print_warning()
            decision = input("Would you like to Move (m) or shoot (s) ")
            try:
                if decision == "m":
                    location = int(input("Which room {} ".format(self.cave.get(self.playerPos))))
                    self.move(location)
                    keepGoing = self.gameOver(location)
                elif decision == "s":
                    location = int(input("Which room {} ".format(self.cave.get(self.playerPos))))
                    keepGoing = self.shoot(location)
                elif decision == "q":
                    keepGoing = 0;
                else:
                    print("Please choose 'm', 's', or 'q'")
            except ValueError:
                print("Please choose 'm', 's', or 'q'")


if __name__ == '__main__':
    test = WumpusGame()
    test.gamePlay()
