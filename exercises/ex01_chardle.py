"""EX01 - Chardle - A Cute Step Toward Wordle."""
__author__ = "730550191"


word_guess: str = input("Enter a 5-character word ")
if len(word_guess) != 5:
    print("Error: Word must contain 5 characters.")
    exit()

letter_guess: str = input("Enter a single character ")
if len(letter_guess) != 1:
    print ("Error: Character must be a single character.")
    exit()

print("Searching for " + letter_guess + " in " + word_guess)

variable_count: int = 0

if word_guess[0] == letter_guess:
    print(letter_guess + " found at index 0")
    variable_count = (variable_count + 1)
    
if word_guess[1] == letter_guess:
    print(letter_guess + " found at index 1")
    variable_count = (variable_count + 1)
    
if word_guess[2] == letter_guess:
    print(letter_guess + " found at index 2")
    variable_count = (variable_count + 1)
    
if word_guess[3] == letter_guess:
    print(letter_guess + " found at index 3")
    variable_count = (variable_count + 1)
    
if word_guess[4] == letter_guess:
    print(letter_guess + " found at index 4")
    variable_count = (variable_count + 1)
    

print(str(variable_count) + " instances of " + letter_guess + " found in " + word_guess)


