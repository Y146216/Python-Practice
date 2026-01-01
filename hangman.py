import getpass

word = getpass.getpass("enter the secret word: ").lower()
guessed_letters = []
chances = 6

while chances > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("🎉 You won the game!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed 😅")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        chances -= 1
        print("Wrong guess ❌")
        print("Chances left:", chances)
    else:
        print("Correct guess ✅")

if chances == 0:
    print("💀 Game Over! The word was:", word)