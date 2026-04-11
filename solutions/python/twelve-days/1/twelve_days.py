def ordinal(n: int) -> str:
    ordinals = ["", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    return ordinals[n]


def recite(start_verse: int, end_verse: int) -> list[str]:
    if start_verse < 1 or end_verse > 12 or start_verse > end_verse:
        raise ValueError("Invalid verse range")

    gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, and",
        "three French Hens,",
        "four Calling Birds,",
        "five Gold Rings,",
        "six Geese-a-Laying,",
        "seven Swans-a-Swimming,",
        "eight Maids-a-Milking,",
        "nine Ladies Dancing,",
        "ten Lords-a-Leaping,",
        "eleven Pipers Piping,",
        "twelve Drummers Drumming,"
    ]

    verses = []
    for verse in range(start_verse, end_verse + 1):
        verse_gifts = gifts[:verse][::-1]
        verse_text = f"On the {ordinal(verse)} day of Christmas my true love gave to me: {' '.join(verse_gifts)}"
        verses.append(verse_text)

    return verses
