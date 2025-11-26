def get_letter_freq(S):
    freq_dict = {}
    for word in S:
        for letter in set(word):
            if letter not in freq_dict:
                freq_dict[letter] = 1
            else:
                freq_dict[letter] += 1
    return freq_dict


#.get is for key access for potentially unimplemented keys
#second arguement is the return if it doesn't exist
def score_guess(guess, letter_freq):
    unique_letters = set(guess)
    score = 0
    for letter in unique_letters:
        score += letter_freq.get(letter, 0) 
    return score