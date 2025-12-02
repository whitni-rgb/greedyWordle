# 🧠 Greedy Wordle Solver

This project is an intelligent agent that solves the game **Wordle** automatically using a **greedy search strategy** and a **letter-frequency heuristic**. The solver repeatedly chooses the best possible guess based on the remaining candidate words, simulates Wordle feedback (`G`, `Y`, `B`), filters the word list, and continues until the correct answer is found.

---

## 📌 Overview

The agent models Wordle as a search problem:

- **State:** the set of all possible remaining answer words  
- **Action:** selecting a guess  
- **Sensor:** receiving Wordle feedback patterns  
- **Actuator:** generating the next guess  
- **Goal:** solve the puzzle within 6 turns  

The solver runs automatically with no human input. You simply provide a secret answer word, and the agent plays a full game against it.

---

## 🧩 PEAS Description

### **Performance**
- Solve Wordle within 6 guesses  
- Efficiently shrink the candidate space  
- Correctly apply Wordle’s G/Y/B feedback rules  
- Maximize information gained per guess  

### **Environment**
- Hidden 5-letter answer  
- Dictionary of possible words  
- Wordle feedback mechanics  

### **Actuators**
- Produces a guess each turn

### **Sensors**
- Simulated feedback (`G`, `Y`, `B`) from guessed word  
- Updated list of valid remaining answers

---

## 🧠 System Architecture

The project is modularized into separate files:

### **`heuristic.py`**
- `get_letter_freq(S)`: calculates letter frequencies in the remaining candidate set  
- `score_guess(word, freq)`: scores a word based on distinct-letter frequencies  

### **`feedback.py`**
- `feedback_pattern(guess, answer)`: generates the Wordle feedback pattern  
- `matches_feedback(word, guess, pattern)`: checks consistency of a candidate word with feedback  

### **`solver.py`**
Implements the main greedy solving loop:

1. Load all words into candidate set `S`
2. Compute letter frequencies over `S`
3. Score candidates and pick the highest-scoring guess  
4. Generate feedback using `feedback_pattern`
5. Filter `S` using `matches_feedback`
6. Repeat until:
   - Pattern is `"GGGGG"`  
   - Only one candidate remains  
   - Six turns have passed  

### **`main.py`**
Simple entry point:

```python
from solver import solve
solve("cigar")
