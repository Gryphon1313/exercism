def line_up(name: str, number: int) -> str:
    suffix = "th"
    if number % 10 == 1 and number % 100 != 11:
        suffix = "st"
    elif number % 10 == 2 and number % 100 != 12:
        suffix = "nd"
    elif number % 10 == 3 and number % 100 != 13:
        suffix = "rd"
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"