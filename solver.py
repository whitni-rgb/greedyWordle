def get_words():
    wordlist =[]
    with open("words.txt", "r") as words:
        for word in words:
            stripped = word.strip().lower()
            wordlist.append(stripped)
    return wordlist

def get_letter_freq(S):
    freq_dict = {}
    for word in S:
        for letter in set(word):
            if letter not in freq_dict:
                freq_dict[letter] = 1
            else:
                freq_dict[letter] += 1
    return freq_dict

words = get_words()
get_letter_freq(words)