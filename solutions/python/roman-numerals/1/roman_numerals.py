def roman(number: int) -> str:
    if number <= 0 or number >= 4000:
        raise ValueError("input out of range")

    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_numeral = ''
    for i in range(len(val)):
        count = number // val[i]
        roman_numeral += syms[i] * count
        number -= val[i] * count
    return roman_numeral

