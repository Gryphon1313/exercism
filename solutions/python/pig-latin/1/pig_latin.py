def work_on_word(text: str) -> str:
    vowels = "aeiou"
    qu_index = text.lower().find("qu")
    y_index = text.lower().find("y")
    if text[0].lower() in vowels or text[0:2].lower() in ["xr", "yt"]:
        return text + "ay"
    elif qu_index >= 0 and (qu_index == 0 or text[qu_index - 1].lower() not in vowels):
        return text[qu_index + 2:] + text[:qu_index + 2] + "ay"

    elif text[0].lower() not in vowels and y_index >= 1 and y_index < len(text) - 1:
        return text[y_index:] + text[:y_index] + "ay"
    elif text[0].lower() not in vowels:
        first_vowel_index = -1
        for i in range(1, len(text)):
            if text[i].lower() in vowels:
                first_vowel_index = i
                break
        
        return text[first_vowel_index:] + text[:first_vowel_index] + "ay"


def translate(text: str) -> str:
    words = text.split()
    translated_words = [work_on_word(word) for word in words]
    return " ".join(translated_words)