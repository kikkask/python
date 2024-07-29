import random
# Função
def game():

    print("\nWelcome to the Hangman Game!")
    print("Guess the word below (hint: fruit):\n")

    words = ['banana','avocado','grape','strawberry','orange']

    word = random.choice(words)

    lettersUncovered = ['_' for letter in word]

    chances = 6

    wrongLetters = []

    while chances > 0:

        print(" ".join(lettersUncovered))
        print("Remaining chances:", chances)
        print("Wrong letters:", " ".join(wrongLetters))

        attempt = input("Type one letter: ").lower()

        if attempt in word:
            index = 0
            for letter in word:
                if attempt == letter:
                    lettersUncovered[index] = letter
                index += 1
        else:
            chances -= 1
            wrongLetters.append(attempt)

        if '_' not in lettersUncovered:
            print("\nYou WIN!! Congrats!!, the word was:", word)
            break

    if '_' in lettersUncovered:
        print("\nYou LOST!! The word was:", word)

# Bloco main
if __name__ == "__main__":
    game()
    print("\nGame developed by Lucas Brito (kikkask) using Python 3.10.0\n")

