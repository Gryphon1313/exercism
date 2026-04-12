import re
class Luhn:
    def __init__(self, card_num: str):
        self.card_num = card_num

    def valid(self) -> bool:
        test_number = re.sub(r'\s+', '', self.card_num)
        if not test_number or not test_number.isdigit() or len(test_number) <= 1:
            return False

        total = 0
        reverse_digits = test_number[::-1]

        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n

        return total % 10 == 0
