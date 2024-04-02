from random import choice
def choose_random_word():
    words = list(map(str, input().split()))
    word = choice(words)
    return word

def display_word (word,guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman_game():
    word = choose_random_word()
    max_attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Guess the word: ", display_word(word, guessed_letters))

    while '_' in display_word(word, guessed_letters) and max_attempts > 0:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")

        if guess in guessed_letters:
            print("You've already guessed that letter.")

        guessed_letters.append(guess)
        if guess in word:
            print("Correct!")
        else:
            max_attempts -= 1
            print(f"Incorrect guess. You have {max_attempts} attempts.")

        print("Current word: ", display_word(word, guessed_letters))

    if '_' not in display_word(word, guessed_letters):
        print("Congratulations! You've guessed the word:", display_word(word, guessed_letters))
    else:
        print("Sorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman_game()
