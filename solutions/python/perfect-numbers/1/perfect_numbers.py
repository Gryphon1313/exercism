def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    divisors = [i for i in range(1, number) if number % i == 0]
    divisor_sum = sum(divisors)

    if divisor_sum == number:
        return "perfect"
    elif divisor_sum < number:
        return "deficient"
    else:
        return "abundant"
