"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


# define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    if (elapsed_bake_time >= 0):
        # base case, calculate difference between expected and elapsed time
        return EXPECTED_BAKE_TIME - elapsed_bake_time
    elif (elapsed_bake_time >= EXPECTED_BAKE_TIME):
        # handle scenario when elapsed time is greater than needed bake time
        return 0
    # error scenario potential negative number provided as input
    return -1 


# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time needed.

    :param number_of_layers: int - number of layers the lasagna will be.
    :return: int - amount of time needed to prepare the dish (in minutes).

    Function that takes the number of layers the lasagna will be and calculates
    how long it will take to prepare the dish.
    """
    if (number_of_layers >= 0):
        # base case, calculate the time needed
        return PREPARATION_TIME * number_of_layers
    return -1


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the amount of time already elapsed for making the dish.

    :param number_of_layers: int - number of layers the lasagna will be.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - amount of time since starting the lasagna (in minutes).

    Function that takes the number of layers the lasagna will be and how 
    long it has spent in the oven and calculates how long it has been since
    starting the preparation.
    """
    if (number_of_layers < 0 or elapsed_bake_time < 0):
        # error case, negative value for layer count or elapsed time
        return -1
    elif (number_of_layers == 0):
        # 0 layer lasagna, no actual final product
        return 0
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time


