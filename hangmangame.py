import random

words = ['apple', 'banana', 'cherry', 'orange', 'grape']
secret = random.choice(words)

guessed_letters = set()
guessed_words = set()
tries = 0
max_tries = 6

stages = [
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """
]

while tries < max_tries:
    print(stages[tries])
    display = ' '.join([c if c in guessed_letters else '_' for c in secret])
    print("Word:", display)
    print(f"Chances left: {max_tries - tries} / {max_tries}")
    if guessed_letters:
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))
    if guessed_words:
        print("Guessed words:", ', '.join(sorted(guessed_words)))
    print()

    if all(c in guessed_letters for c in secret):
        print("🎉 You win! The word was:", secret)
        break

    guess = input("👉 Guess a letter OR the whole word: ").lower().strip()

    if not guess.isalpha():
        print("Please enter letters only.\n")
        continue

    # Full-word guess
    if len(guess) > 1:
        if guess in guessed_words:
            print("You already tried that word.\n")
            continue
        guessed_words.add(guess)
        if guess == secret:
            print("🎉 Spot on! You guessed the word:", secret)
            break
        else:
            tries += 1
            print(f"❌ Not the word. Chances left: {max_tries - tries}\n")
        continue

    # Single-letter guess
    if guess in guessed_letters:
        print("You already tried that letter.\n")
        continue

    if guess in secret:
        guessed_letters.add(guess)
        print("✅ Correct!\n")
    else:
        guessed_letters.add(guess)
        tries += 1
        print(f"❌ Wrong! Chances left: {max_tries - tries}\n")

if tries == max_tries:
    print(stages[tries])
    print("💀 Game over! The word was:", secret)
