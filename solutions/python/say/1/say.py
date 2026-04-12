def say(number: int) -> str:
    if number == 0:
        return "zero"

    if number < 0 or number >= 1_000_000_000_000:
        raise ValueError("input out of range")

    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]

    words = []
    for i in range(4):
        n = number % 1000
        if n > 0:
            group_words = []
            if n >= 100:
                group_words.append(units[n // 100] + " hundred")
                n %= 100
            if n >= 20:
                ten_word = tens[n // 10]
                unit_digit = n % 10
                if unit_digit > 0:
                    group_words.append(ten_word + "-" + units[unit_digit])
                else:
                    group_words.append(ten_word)
            elif n >= 10:
                group_words.append(teens[n - 10])
            elif n > 0:
                group_words.append(units[n])
            if thousands[i]:
                group_words.append(thousands[i])
            words.insert(0, ' '.join(group_words))
        number //= 1000

    return ' '.join(words).strip()
