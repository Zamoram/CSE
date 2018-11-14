import random
mymoney = 15
rounds = 0

while mymoney > 0:
    diceroll1 = random.randint(1, 6)
    diceroll2 = random.randint(1, 6)
    answer = diceroll1 + diceroll2
    rounds += 1
    mymoney -= 1
    if answer == 7:
        mymoney += 5
        print("YOU WIN!!!!!!!!!!!")
    print(mymoney)
    print("You played %s rounds" % rounds)