import re

def count_words(sentence: str) -> int:
    sentence = re.sub(r'[_,]', ' ', sentence)
    words = re.findall(r"\b[a-zA-Z\d]+(?:'[a-zA-Z\d]+)*\b", sentence.lower())
    
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count