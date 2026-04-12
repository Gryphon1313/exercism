def recite(start, take=1):
    verses = []
    for round in range(take):
        verse_number = start - round
        verses.extend(recite_verse(verse_number))
        if round < take - 1:
            verses.append('')
    return verses

def recite_verse(verse_number):
    number = number_to_str(verse_number)
    next_number = number_to_str(verse_number - 1) if verse_number > 1 else 'one'
    verses = [
        f"{number.capitalize()} green {'bottle' if number == 'one' else 'bottles'} hanging on the wall,",
        f"{number.capitalize()} green {'bottle' if number == 'one' else 'bottles'} hanging on the wall,",
        "And if one green bottle should accidentally fall,",
    ]
    if number == 'one':
        verses.append("There'll be no green bottles hanging on the wall.")
    else:
        verses.append(f"There'll be {next_number} green {'bottle' if next_number == 'one' else 'bottles'} hanging on the wall.")
    
    return verses

def number_to_str(number):
    if number == 0:
        return 'no'
    elif number == 1:
        return 'one'
    elif number == 2:
        return 'two'
    elif number == 3:
        return 'three'
    elif number == 4:
        return 'four'
    elif number == 5:
        return 'five'
    elif number == 6:
        return 'six'
    elif number == 7:
        return 'seven'
    elif number == 8:
        return 'eight'
    elif number == 9:
        return 'nine'
    elif number == 10:
        return 'ten'
    else:
        raise ValueError('number must be between 0 and 10')