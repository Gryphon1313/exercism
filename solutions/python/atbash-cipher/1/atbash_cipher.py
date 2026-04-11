def encode(plain_text: str) -> str:
    ciphered_text = ""
    for char in plain_text.lower():
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            ciphered_char = chr(offset + (25 - (ord(char) - offset)))
            ciphered_text += ciphered_char
        elif char.isdigit():
            ciphered_text += char
        # Ignore non-alphanumeric characters
    return ' '.join(ciphered_text[i:i+5] for i in range(0, len(ciphered_text), 5))


def decode(ciphered_text: str) -> str:
    plain_text = ""
    for char in ciphered_text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            plain_char = chr(offset + (25 - (ord(char) - offset)))
            plain_text += plain_char
        elif char.isdigit():
            plain_text += char
    return plain_text
