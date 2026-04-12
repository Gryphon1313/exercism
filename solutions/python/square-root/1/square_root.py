def square_root(number: int) -> int:
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    if number == 0:
        return 0
    x = number
    while x * x > number:
        x = (x + number // x) // 2
    return x
