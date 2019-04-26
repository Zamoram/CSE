import csv


# def divisble_by_2(num: str):
#     first_num = int(num[0])  # This is the first number
#     if first_num % 2 == 0:
#         return True
#     return False


def validate(num: str):
    if is_first_num_odd(num) and is_second_num_even(num):
        return True
    return False


def divisble_by_three(num: str):
    first_num = int(num[0])  # This is the first number
    if first_num % 3 == 0:
        return True
    return False


def divisble_by_2(num: str):
    first_num = int(num[0])  # This is the first number
    if first_num % 2 == 0:
        return True
    return False


def is_first_num_odd(num: str):
    first_num = int(num[0])
    if first_num % 2 == 1:
        return True
    return False

def is_second_num_even(num: str):


# with open("Book1.csv", 'r') as old_csv:
#     reader = csv.reader(old_csv)
#     for row in reader:
#         # print(int(old_number) + 1)
#         old_number = row[0]
#         print(old_number)
# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Processing...")
#
#         for row in reader:
#             # old_number = int(row[0]) + 1
#             old_number = row[0] # This is a string
#             first_num = int(old_number[0])
#             if first_num == 4:
#                 writer.writerow(row)
#             # print(int(old_number) + 1)
#             # print(old_number)
#     print("Done")


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        print("Writing file")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            # old_number = int(row[0]) + 1
            old_number = row[0]  # This is a string
            if validate(old_number):
                writer.writerow(row)
            # print(int(old_number) + 1)
            # print(old_number)
print("Done")
