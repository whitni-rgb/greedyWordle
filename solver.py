from heuristic import get_letter_freq, score_guess
from feedback import feedback_pattern, matches_feedback


def get_words():
    wordlist =[]
    with open("words.txt", "r") as words:
        for word in words:
            stripped = word.strip().lower()
            wordlist.append(stripped)
    return wordlist



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