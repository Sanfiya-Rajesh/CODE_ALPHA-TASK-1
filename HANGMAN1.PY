import random

# List of possible words for the game
word_list = ['python', 'hangman', 'challenge', 'programming', 'developer', 'computer']

# Function to display the current state of the word
def display_word(word, guessed_letters):
    displayed = ''
    for letter in word:
        if letter in guessed_letters:
            displayed += letter + ' '
        else:
            displayed += '_ '
    return displayed.strip()

# Main Hangman function
def hangman():
    # Randomly select a word from the word_list
    word = random.choice(word_list)
    guessed_letters = []  # To store the correct guesses
    incorrect_guesses = []  # To store incorrect guesses
    attempts_left = 6  # Number of incorrect guesses allowed

    print("Welcome to Hangman Game!")
    print("Try to guess the word.")
    
    while attempts_left > 0:
        # Show current word status
        print("\nWord: " + display_word(word, guessed_letters))
        print("Incorrect guesses: ", " ".join(incorrect_guesses))
        print(f"Attempts left: {attempts_left}")
        
        # Get the player's guess
        guess = input("Guess a letter: ").lower()

        # Ensure the guess is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue
        
        # Check if the letter was already guessed
        if guess in guessed_letters or guess in incorrect_guesses:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        # Check if the guess is correct
        if guess in word:
            guessed_letters.append(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses.append(guess)
            attempts_left -= 1
            print(f"Oops! '{guess}' is not in the word.")
        
        # Check if the player has won
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nSorry! You've run out of attempts. The word was: {word}")

# Run the game
if __name__ == "__main__":
    hangman()
