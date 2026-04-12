def decode(string: str) -> str:
    if not string:
        return ""

    decoded = []
    i = 0
    while i < len(string):
        if string[i].isdigit():
            # Parse the full number
            num_str = ""
            while i < len(string) and string[i].isdigit():
                num_str += string[i]
                i += 1
            count = int(num_str)
        else:
            count = 1

        if i < len(string):
            char = string[i]
            decoded.append(char * count)
            i += 1

    return ''.join(decoded)


def encode(string: str) -> str:
    if not string:
        return ""

    encoded = []
    count = 1
    prev_char = string[0]

    for char in string[1:]:
        if char == prev_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(prev_char)
            prev_char = char
            count = 1

    # Handle the last run
    if count > 1:
        encoded.append(str(count))
    encoded.append(prev_char)

    return ''.join(encoded)
