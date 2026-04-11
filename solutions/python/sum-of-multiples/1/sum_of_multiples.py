def sum_of_multiples(limit: int, multiples: list) -> int:
    if not multiples:
        return 0

    total = 0
    for i in range(limit):
        if any(i % m == 0 for m in multiples if m != 0):
            total += i

    return total
