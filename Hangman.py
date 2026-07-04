import random

# List of predefined words
words = ["python", "computer", "program", "developer", "intern"]

# Choose a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("=" * 40)
print("       WELCOME TO HANGMAN")
print("=" * 40)
print("Guess the hidden word one letter at a time.")
print(f"You have {max_wrong} incorrect guesses.\n")

while wrong_guesses < max_wrong:

    # Display the word
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if the player has guessed all letters
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        wrong_guesses += 1
        print("❌ Wrong!")
        print("Remaining attempts:", max_wrong - wrong_guesses)

# If player loses
if wrong_guesses == max_wrong:
    print("\n💀 Game Over!")
    print("The correct word was:", word)

print("\nThanks for playing Hangman!")