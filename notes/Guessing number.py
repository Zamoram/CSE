import random  # This should be on line 1

answer = random.randint(1, 10)
guesses = 5
playing = True
wrong = False
while playing and guesses > 0:
    guess = input("Choose a number from 1 and 10")
    if int(guess) == int(answer):
        print("You have won")
        playing = False

    else:
        print("Try Again!!!!")
        guesses -= 1
        if int(guess) > int(answer):
            print("Too High")
        if int(guess) < int(answer):
            print("Too Low")

