import random
class Dice:
    roll = (1, 2, 3, 4, 5, 6)
    
    def random_pick(self):
        numbers = random.choice(Dice.roll)
        return numbers

    def random_pick_even(self):
        even_numbers = list(filter(lambda x: x % 2 == 0, Dice.roll))
        picked_even = random.choice(even_numbers)
        return picked_even

    def random_pick_odd(self):
        odd_numbers = list(filter(lambda x: x % 2 != 0, Dice.roll))
        picked_odd = random.choice(odd_numbers)
        return picked_odd


dice1 = Dice()
dice2 = Dice()
dice3 = Dice()
value1 = dice1.random_pick()
value2 = dice2.random_pick_even()
value3 = dice3.random_pick_odd()
print(f"({value1}, {value2}, {value3})")

