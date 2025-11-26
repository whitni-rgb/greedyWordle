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


#.get is for key access for potentially unimplemented keys
#second arguement is the return if it doesn't exist
def score_guess(guess, letter_freq):
    unique_letters = set(guess)
    score = 0
    for letter in unique_letters:
        score += letter_freq.get(letter, 0) 
    return score

def choose_best_guess(S):
    best_score = -1
    best_word = None 
    letter_f = get_letter_freq(S)
    for word in S:
        score = score_guess(word, letter_f)
        if score > best_score:
            best_score = score
            best_word  = word
    return best_word

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


def solve(answer):
    turn=0
    S = get_words()
    for i in range(6):
        guess = choose_best_guess(S)
        print("Turn", turn+1, "guess:", guess)

        pattern = feedback_pattern(guess, answer)
        print("Feedback:", pattern)

        turn +=1

        if pattern == "GGGGG":
            print("Solved in", turn+1, "turns!")
            return guess
        
        new_S = []
        for word in S:
            if matches_feedback(word, guess, pattern):
                new_S.append(word)
        S = new_S

        if len(S) == 0:
            print("No candidates left — something is inconsistent.")
            return None
        if len(S) == 1:
            print("Only one candidate left:", S[0])
            return S[0]

    # If we finish the loop with no solution:
    print("Failed to solve in 6 turns.")
    return None


solve("cigar") 
# words = get_words()

# print(choose_best_guess(words))
    

   
   




# print(score_guess("race", letter_f))