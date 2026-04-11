def is_valid(isbn: str) -> bool:
    # Remove hyphens and check if the length is 10
    isbn = isbn.replace('-', '').upper()
    if len(isbn) != 10:
        return False

    # Check if the first 9 characters are digits and the last character is a digit or 'X'
    if not (isbn[:9].isdigit() and (isbn[9] == 'X' or isbn[9].isdigit())):
        return False

    # Calculate the checksum
    total = sum(int(digit) * (10 - i) for i, digit in enumerate(isbn[:9]))
    if isbn[9] == 'X':
        total += 10 * 1
    else:
        total += int(isbn[9]) * 1

    # Check if the checksum is divisible by 11
    return total % 11 == 0
