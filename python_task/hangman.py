import random

# 1. Word List
words = ["python", "code", "alpha", "hangman", "intern"]
word = random.choice(words)
guessed = ['_'] * len(word)
attempts = 6
guessed_letters = []

# 2. Game Loop
while attempts > 0 and '_' in guessed:
    print("\nCurrent Word:", ' '.join(guessed))
    print("Guessed Letters:", ', '.join(guessed_letters))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("Correct guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! {attempts} attempts left.")

# 3. Result
if '_' not in guessed:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost. The word was:", word)
