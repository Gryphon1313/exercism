def proverb(*items: list[str], qualifier: str) -> list[str]:
    if not items:
        return []
    lines = []
    if qualifier is None:
        qualifier = items[0]
    else:
        qualifier = f"{qualifier} {items[0]}"
    
    for i in range(len(items) - 1):
        lines.append(f"For want of a {items[i]} the {items[i + 1]} was lost.")
    
    lines.append(f"And all for the want of a {qualifier}.")
    
    return lines
