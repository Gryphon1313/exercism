def prime(number: int) -> int:
    if number == 0:
        raise ValueError("there is no zeroth prime")
    if number < 1:
        raise ValueError("input must be a positive integer")

    primes = []
    num = 2
    while len(primes) < number:
        is_prime = True
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1

    return primes[-1]
