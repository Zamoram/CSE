test_num = "6151359320238050"

def validate(num: str):
#Use this for odd numbers    for index in range(len(num)):
#Use this for odd numbers        int_version = int(num[index])
        pass

print(validate(test_num))
num_list = list(test_num)
num_list.pop(15)
print(num_list)


def reverse_test_num(string):
    return string[15:0]
    

print(reverse_test_num("6151359320238050"))
