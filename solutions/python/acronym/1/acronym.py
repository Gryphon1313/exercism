def abbreviate(words: str) -> str:
    punctuation = set('-_')
    for p in punctuation:
        words = words.replace(p, ' ')
    return ''.join(word[0].upper() for word in words.split() if word[0].isalpha())
