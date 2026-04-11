def is_isogram(string: str) -> bool:
    cleaned = [char.lower() for char in string if char.isalnum()]
    return len(cleaned) == len(set(cleaned))