def make_diamond_row(letter: str, width: int) -> str:
    if letter == 'A':
        return 'A'.center(width, ' ')
    else:
        spaces_between = 2 * (ord(letter) - ord('A')) - 1
        row = letter + ' ' * spaces_between + letter
        return row.center(width, ' ')


def make_letter_list(letter: str) -> list:
    increasing_list = [chr(i) for i in range(ord('A'), ord(letter) + 1)]
    return increasing_list + increasing_list[-2::-1]


def rows(letter: str) -> list:
    if letter == 'A':
        return ['A']
    else:
        letter_list = make_letter_list(letter)
        width = 2 * (ord(letter) - ord('A')) + 1
        return [make_diamond_row(l, width) for l in letter_list]
