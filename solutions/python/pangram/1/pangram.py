def is_pangram(sentence: str) -> bool:
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet.issubset(set(sentence.lower()))