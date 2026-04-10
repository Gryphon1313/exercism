def is_armstrong_number(number: int) -> bool:
    # An Armstrong number is an n-digit number that is equal to the sum of its 
    # own digits each raised to the power of n.
    digits = [int(d) for d in str(number)]
    n = len(digits)
    return sum(d ** n for d in digits) == number
