import random
mymoney = 15

diceroll1 = random.randint(1, 6)
diceroll2 = random.randint(1, 6)
answer = diceroll1 + diceroll2
if answer == 7:
    print("YOU WIN!!!!!!!!!!!")