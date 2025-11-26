def feedback_pattern(guess, answer):
    pattern = []
    for i in range(len(answer)):
        if guess[i] == answer[i]:
            pattern.append("G")
        elif guess[i] in answer:
            pattern.append("Y")
        elif guess[i] not in answer:
            pattern.append("B")
    return "".join(pattern)


def matches_feedback(word, guess, pattern):
    for i in range(len(pattern)):
        if pattern[i] == "G":
            if word[i] != guess[i]:
                return False
        elif pattern[i] == "Y":
            if guess[i] not in word or guess[i] == word[i]:
                return False
        elif pattern[i] == "B": #duplicates problem
            if guess[i] in word:
                return False
    return True