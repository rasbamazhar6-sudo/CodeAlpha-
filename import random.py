import random

# Hangman drawings for each wrong attempt
hangman_stages = [
    """
       _______
      |       |
      |       
      |      
      |      
      |      
    __|__
    """,
    """
       _______
      |       |
      |       O
      |      
      |      
      |      
    __|__
    """,
    """
       _______
      |       |
      |       O
      |       |
      |      
      |      
    __|__
    """,
    """
       _______
      |       |
      |       O
      |      /|
      |      
      |      
    __|__
    """,
    """
       _______
      |       |
      |       O
      |      /|\\
      |      
      |      
    __|__
    """,
    """
       _______
      |       |
      |       O
      |      /|\\
      |      / 
      |      
    __|__
    """,
    """
       _______
      |       |
      |       O
      |      /|\\
      |      / \\
      |      
    __|__
    """
]

# Predefined list of words
words = ["apple", "house", "river", "chair", "bread"]

# Pick a random word
secret_word = random.choice(words)

guessed_letters = []
attempts_left = 6
display_word = ["_"] * len(secret_word)

print("=== Welcome to Hangman ===")
print("Guess the word letter by letter!")
print("You have 6 incorrect guesses.\n")

# Game loop
while attempts_left > 0 and "_" in display_word:
    print("Word:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Attempts left:", attempts_left)
    
    # Show hangman based on wrong attempts done so far
    wrong_attempts = 6 - attempts_left
    print(hangman_stages[wrong_attempts])

    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!\n")
        # Reveal letters
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong guess!\n")
        attempts_left -= 1

# End of game
print("\n=== FINAL RESULT ===")
print(hangman_stages[6 - attempts_left])  # Final hangman figure
print("The word was:", secret_word)

if "_" not in display_word:
    print("🎉 You WIN! Great job!")
else:
    print("❌ You LOST! Better luck next time.")
