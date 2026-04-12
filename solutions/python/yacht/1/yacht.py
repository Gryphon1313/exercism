# Score categories.
# Change the values as you see fit.
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12


def score(dice: list, category) -> int:
    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0
    elif category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        return sum(die for die in dice if die == category - 1)
    elif category == FULL_HOUSE:
        unique_dice = set(dice)
        if len(unique_dice) == 2 and all(dice.count(die) in (2, 3) for die in unique_dice):
            return sum(dice)
        return 0
    elif category == FOUR_OF_A_KIND:
        for die in set(dice):
            if dice.count(die) >= 4:
                return die * 4
        return 0
    elif category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
    elif category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
    elif category == CHOICE:
        return sum(dice)
    else:
        raise ValueError("Invalid category")
