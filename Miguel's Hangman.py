import random

word_bank = ["computer", "table", "monitor", "python", "rhythm", "gypsy", "myth", "microwave", "class", "teacher"]
word = random.choice(word_bank)
word = 'pizza'
print(word)
lives = 8
letters_guessed = []
while lives > 0:
    # Show the hidden word
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(output)

    # Take in a guess
    letter_guessed = input("Type in a letter: ")
    letters_guessed.append(letter_guessed)


    lives -= 1



