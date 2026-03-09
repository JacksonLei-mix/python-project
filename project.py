import random

print("Let's play hangman!")

word_bank = ["horse", "apple", "tiger", "pizza", "robot", "banana", "orange"]

while True:

    word = random.choice(word_bank)
    lives = 6
    guessed_letters = []
    display = ["_"] * len(word)

    print("New game starts!")
    while lives > 0 and "_" in display:
        print("\nWord:", " ".join(display))
        print("Lives left:", lives)
        guess = input("Guess a letter: ").lower()
        if guess == "help":
            print("Used letters:", ", ".join(guessed_letters))
            continue
        if guess.startswith("guess "):
            attempt = guess.split(" ", 1)[1]
            if attempt == word:
                display = list(word)
                break
            else:
                lives = 0
                break
        if len(guess) != 1 or not guess.isalpha():
            print("Not a valid guess. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            lives -= 1
            print("Letter not found!")

    if "_" not in display:
        print("\nWord:", " ".join(display))
        print("Word guessed, you've won!")
    else:
        print("\nOut of lives, game over!")
        print("The word was:", word)

    while True:
        again = input("Play again? (yes/no): ").lower()

        if again == "yes":
            break
        elif again == "no":
            print("Thanks for playing!")
            exit(0)
        else:
            print("Invalid input. Play again? (yes/no)")
