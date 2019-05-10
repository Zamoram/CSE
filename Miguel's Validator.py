test_num = "4556737586899855"


def validate(num: str):
    num_list = list(num)
    last_num = int(num_list.pop(15))
    reverse_form = reverse_it(num_list)
    print(reverse_form)
    for index in range(len(reverse_form)):
        reverse_form[index] = int(reverse_form[index])
        for index in range(len(reverse_form)):  # This is for the odd numbered positions but it needs work.
            reverse_form[index] = int(reverse_form[index])
    print(reverse_form)
for num_list in range(len(test_num)):
    if test_num[num_list] ==

def remember_last_digit(num: str):
    last_num = int(num[0])  # This needs work on, this is to remember the last digit.
    if last_num % 2 == 0:
        return True
    return False


def reverse_it(test_num):
    return test_num[::-1]


print(validate(test_num))

