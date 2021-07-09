import random


# from numpy import roll
# dice_sides = tuple(range(1,7))
# sides = random.choices(dice_sides,k=2)
# side2 = random.choice(dice_sides)
# print(tuple(sides))

class Dice:
     def roll(self):
        dice_sides = tuple(range(1,7))
        sides = random.choices(dice_sides,k=2)
        print(tuple(sides))

challenge_1 = Dice()
challenge_1.roll() 

# NOTE Alternative

class Dice2:
    def rolling(self):
        side1 = random.randint(1,7)
        side2 = random.randint(1,7)
        return side1,side2

dice = Dice2()
print(dice.rolling())