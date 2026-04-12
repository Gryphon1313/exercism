import re


class PhoneNumber:
    def __init__(self, number: str):
        if re.search(r'[A-Za-z]', number):
            raise ValueError("letters not permitted")

        if number.count('+') > 1 or ('+' in number and not number.strip().startswith('+')):
            raise ValueError("punctuations not permitted")

        allowed_chars = set('0123456789-(). +')
        for char in number:
            if char not in allowed_chars:
                raise ValueError("punctuations not permitted")

        digits = ''.join(filter(str.isdigit, number))

        if len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(digits) == 11:
            if digits[0] != '1':
                raise ValueError("11 digits must start with 1")
            digits = digits[1:]

        if digits[0] == '0':
            raise ValueError("area code cannot start with zero")
        if digits[0] == '1':
            raise ValueError("area code cannot start with one")
        if digits[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        if digits[3] == '1':
            raise ValueError("exchange code cannot start with one")

        self.number = digits

    @property
    def area_code(self) -> str:
        return self.number[:3]

    def pretty(self) -> str:
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"
    
