import re


def answer(question: str) -> int:
    if not question.startswith("What is ") or not question.endswith("?"):
        raise ValueError("syntax error")

    expression = question[len("What is "):-1].strip()
    if not expression:
        raise ValueError("syntax error")

    expression = re.sub(r"\bmultiplied by\b", "multiplied_by", expression)
    expression = re.sub(r"\bdivided by\b", "divided_by", expression)
    tokens = expression.split()

    if not tokens:
        raise ValueError("syntax error")

    def token_type(token: str) -> str:
        if re.fullmatch(r"-?\d+", token):
            return "NUMBER"
        if token in {"plus", "minus", "multiplied_by", "divided_by"}:
            return "OP"
        return "UNKNOWN"

    parsed_tokens = [(token_type(token), token) for token in tokens]

    for token_type_name, token in parsed_tokens:
        if token_type_name == "UNKNOWN":
            raise ValueError("unknown operation")

    if len(parsed_tokens) == 1 and parsed_tokens[0][0] == "NUMBER":
        return int(parsed_tokens[0][1])

    if len(parsed_tokens) % 2 == 0:
        raise ValueError("syntax error")

    if parsed_tokens[0][0] != "NUMBER":
        raise ValueError("syntax error")

    for index in range(1, len(parsed_tokens), 2):
        if parsed_tokens[index][0] != "OP":
            raise ValueError("syntax error")
        if parsed_tokens[index + 1][0] != "NUMBER":
            raise ValueError("syntax error")

    result = int(parsed_tokens[0][1])
    for index in range(1, len(parsed_tokens), 2):
        op = parsed_tokens[index][1]
        number = int(parsed_tokens[index + 1][1])
        if op == "plus":
            result += number
        elif op == "minus":
            result -= number
        elif op == "multiplied_by":
            result *= number
        elif op == "divided_by":
            result //= number
        else:
            raise ValueError("unknown operation")

    return result
