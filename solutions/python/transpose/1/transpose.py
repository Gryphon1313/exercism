def transpose(text: str) -> str:
    lines = text.splitlines()
    if not lines:
        return ''
    rows = [row.replace(' ', '_') for row in lines]
    max_len = len(max(rows, key=len))
    rows = [row.ljust(max_len) for row in rows]
    rows = [''.join(row) for row in zip(*rows)]
    rows = [row.rstrip().replace('_', ' ') for row in rows]
    return '\n'.join(rows)

