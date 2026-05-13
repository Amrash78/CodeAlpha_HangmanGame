import random

words = ["python", "java", "javascript", "cpp", "html", "css"]

while True:                           

    word = random.choice(words)
    guessed = []
    wrong = 0

    print("\nWelcome to Hangman!")

    while wrong < 6:

        # Show current word progress
        for letter in word:
            if letter in guessed:
                print(letter, end="")
            else:
                print("-", end="")
        print()

        # Check win condition
        win = True
        for letter in word:
            if letter not in guessed:
                win = False

        if win:
            print("You won!")
            break

        # Take input
        guess = input("Guess a letter: ").lower()

        if guess in guessed:
            print("Already guessed!")
        elif guess in word:
            guessed.append(guess)
            print("Correct!")
        else:
            guessed.append(guess)
            wrong += 1
            print("Wrong! Lives left:", 6 - wrong)

    if wrong == 6:
        print("Game over!")
        print("The word was:", word)

    # ── Play again ──────────────────────────────
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing, bye! ")
        break                          
            