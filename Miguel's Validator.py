test_num = "6151359320238050"


def validate(num: str):
    for index in range(len(My_List)):
        My_List[index] = int(My_List[index])
        for index in range(len(num)):  # This is for the odd numbered positions but it needs work.
            test_num = int(num[index])


My_List = list(test_num)
print(My_List)
print(len(My_List))


print(validate(test_num))
num_list = list(test_num)
num_list.pop(15)
print(num_list)


def remember_last_digit(num: str):
    last_num = int(num[0])  # This needs work on, this is to remember the last digit.
    if last_num % 2 == 0:
        return True
    return False


def reverse_it(test_num):
    return test_num[::-1]


print(reverse_it("615135932023805"))