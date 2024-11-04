import random





def run_game():
    game_on = True
    word_list = [
        "python", "challenge", "developer", "algorithm", "function",
        "variable", "computer", "programming", "syntax", "condition",
        "iteration", "loop", "dictionary", "integer", "boolean",
        "exception", "operator", "module", "object", "syntax"
    ]

    lives = 8

    word = random.choice(word_list)
    hidden_answer = []
    guess_letters = []
    display_word = ["_"] * len(word)


    while game_on:


        print("The word is ....\n")
        print(" ".join(display_word))
        print(f"You have {lives} lives remaining")
        guess = input("Enter a letter")

        if len(guess) != 1 or not guess.isalpha():  # Check for valid input
            print("Please enter a single letter.")
            continue

        if guess in guess_letters:
            print("You've already guessed that letter.")
            continue  # Skip the rest of the loop if the letter has already been guessed


        if guess in word:
            for index,letter in enumerate(word):
                if letter == guess:
                    display_word[index] = guess
            print("That is  correct good guess")
        elif guess != word:
            print("THAT IS WRONG")
            lives -= 1

        if lives == 0 :
            print("Youve been HANGED AND YOU DIED GAME OVER")
            break
        elif "_" not in display_word:
            print(f"You won the word was {word}")
            break


while True:
    run_game()
    play_again = input("Would you like to play again yes or no")
    if play_again != "yes":
        print("Thanks for playing man goodbye")
        break