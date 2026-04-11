def label(colors: list[str]) -> str:
    color_values = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }
    total = color_values[colors[0]] * 10 + color_values[colors[1]]
    total = total * (10 ** color_values[colors[2]])
    if total >= 1_000_000_000:
        return f"{total // 1_000_000_000} gigaohms"
    if total >= 1_000_000:
        return f"{total // 1_000_000} megaohms"
    if total >= 1000:
        return f"{total // 1000} kiloohms"
    return f"{total} ohms"
