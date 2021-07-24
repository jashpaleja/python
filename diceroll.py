import random

class Dice:
    def roll(self):
        a = random.randint(1,6)
        p = random.randint(1,6)
        return a, p


dice = Dice()
print(dice.roll())