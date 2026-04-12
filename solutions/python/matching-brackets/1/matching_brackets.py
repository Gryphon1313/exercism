def is_paired(input_string: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in input_string:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0
