def equilateral(sides: list[int]) -> bool:
    if not valid(sides):
        return False
    return len(set(sides)) == 1


def isosceles(sides: list[int]) -> bool:
    if not valid(sides):
        return False
    return len(set(sides)) <= 2

def scalene(sides: list[int]) -> bool:
    if not valid(sides):
        return False
    return len(set(sides)) == 3

def valid(sides: list[int]) -> bool:
    if not sides or len(sides) != 3:
        return False
    a, b, c = sorted(sides)
    if a <= 0:
        return False
    return a + b >= c