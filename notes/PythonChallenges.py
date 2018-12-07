# Challenge 1
def challenge1(firstname, lastname):
    print(lastname, firstname)
challenge1("Miguel", "Zamora")


# Challenge 4
def challenge4(number):
    if number < 0:
        return"negative"
    if number > 0:
        return"positive"
    if number == 0:
        return"Zero"
    print(challenge4(5))


# Challenge 3
def challenge3(b, h):
    return 5 * b * h
print(challenge3(3, 6))
