def score(word: str) -> int:
    letter_scores = {
        1: "AEIOULNRST",
        2: "DG",
        3: "BCMP",
        4: "FHVWY",
        5: "K",
        8: "JX",
        10: "QZ"
    }
    
    total_score = 0
    for letter in word.upper():
        for score, letters in letter_scores.items():
            if letter in letters:
                total_score += score
                break
    return total_score
