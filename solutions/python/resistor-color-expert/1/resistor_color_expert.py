def resistor_label(colors: list[str]) -> str:
    color_codes = {
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

    tolerance_codes = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%"
    }

    if len(colors) == 1:
        return "0 ohms"
    base_number = 0
    if len(colors) == 4:
        base_number = color_codes[colors[0]] * 10 + color_codes[colors[1]]
    elif len(colors) == 5:
        base_number = color_codes[colors[0]] * 100 + color_codes[colors[1]] * 10 + color_codes[colors[2]]
    multiplier = 10 ** color_codes[colors[-2]]
    resistance_value = base_number * multiplier
    tolerance = tolerance_codes[colors[-1]]

    return_value = ""
    if resistance_value >= 1_000_000:
        calculated_value = resistance_value / 1_000_000
        if calculated_value.is_integer():
            calculated_value = int(calculated_value)
        return_value = f"{calculated_value} megaohms"
    elif resistance_value >= 1_000:
        calculated_value = resistance_value / 1_000
        if calculated_value.is_integer():
            calculated_value = int(calculated_value)
        return_value = f"{calculated_value} kiloohms"
    else:
        return_value = f"{resistance_value} ohms"

    return f"{return_value} ±{tolerance}"