"""
print("Hello World!")
# Apparently I'm going to slow, so I will speed up
# This is a comment
# This has no effect on the code
# This is used for a variety of things, such as
# 1. Making personal notes about my code
# 2. Commenting out code that does not work
print("Notice what is happening here.")
print()  # This creates a new line
print()  # Do you notice the underline here?
# Hover over top it to see what is wrong.
# Math
print(5 + 3)
print(5 - 3)
print(4 * 5)
print(6 / 5)
print()
# Semi-advanced math
print("Figure this out...")
print(6 // 4)
print(12 // 3)
print(9 // 4)  # This will ONLY give me a whole number
print()
print("Figure this out too...")
print(6 % 4)
print(5 % 3)
print(9 % 4)
# Defining Variables
car_name = "Wiebe mobile"  # String
car_type = "Tesla"  # String
car_cylinders = 16  # Integer
car_miles_per_gallon = 0.01  # Float
print("I have a car called %s. It's pretty nice." % car_name)
print("It has %d cylinders, but gets %f mpg" % (car_cylinders, car_miles_per_gallon))
# Taking Input
name = input("What is your name? ")
print("Hello %s" % name)
age = input("How old are you?")
print("%s? You belong in a museum!" % age)
# Recasting
real_age = int(input("How old are you again? "))
hidden_age = real_age + 5
print(hidden_age)
"""

# Multi-line Comments

"""
This is a multi-line comment
anything in between them is automatically commented out.
"""


# Defining Functions
def say_it():
    print("Hello World!")


say_it()
say_it()
say_it()


# f(x) = 2x + 3
def f(x):
    print(2*x + 3)


f(1)
f(5)
f(5000)


def distance(x1, y1, x2, y2):
    dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print(dist)


distance(0, 0, 3, 4)
distance(0, 0, 5, 12)

# For loops
for i in (1, 2, 3):
    say_it()

for i in range(5):  # Range(5) gives the numbers 0-4
    f(i)

for i in range(5):
    print(i**2)

# While loops
a = 0
while a < 10:
    print(a)
    a += 1  # This is the same as a = a + 1


"""
Hints for loops:
For loops - Use when you know EXACTLY how many iterations
While loops - Use when you DON'T know how many iterations
"""


# Control Statements (If statements)
sunny = False
if sunny:
    print("Go outside")


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


your_grade = grade_calc(82)
print(your_grade)

# Random numbers
import random  # This should be on line 1
print(random.randint(0, 100))

# Equality Statements
print(5 > 3)
print(5 >= 3)
print(3 == 3)
print(3 != 4)
"""
a = 3  # A is set to 3
a == 3 # Is a equal to 3?
"""

# Creating a list
fruit = ['apples', 'oranges', 'blackberries', 'strawberries',
         'blueberries', "raspberries", "pineapple", "mango", "coconut"]  # USE SQUARE BRACKETS!!!!!!
print(fruit)

# Pulling items from a list
print(fruit[1])

# Getting the length of a list
print(len(fruit))
print("The length of the list is %d" % len(fruit))

# Modifying Lists
fruit[8] = 'Banana'
print(fruit)

# Looping through Lists
for item in fruit:
    print(item)

'''
1. Make a list
2. change the 3rd thing in the list
3. print the item
4. print the full list
'''

new_list = ["eggs", "cheese", "oranges", "raspberries"]
new_list[2] = "apples"
print("The last thing in the list is %s" % new_list[len(new_list) - 1])

food_list = ["pizza", "tamales", "tacos", "pie", "enchiladas", "burrito",
             "sushi", "poke", "flan", "poutine", "noodles", "chicken",
             'chili', "Hot wings", "salmon", "chips", "lasagna", "soup",
             "fettuccine", "salad", "carne asada"]

# Slicing
print(food_list[2:5])
print(food_list[3:4])
print(food_list[10:])
print(food_list[:5])

# Adding stuff to a list (part 1)
food_list.append("oranges")
food_list.append("bacon")
print(food_list)
# Everything is in the form Object.method(parameters)

# Adding to a list (not at the end)
food_list.insert(2, "Goat")
print(food_list)

# Removing from a list
food_list.remove("tacos")
food_list.remove("pie")
print(food_list)
# This removes the specific item from the list

# Removing from a list (pt 2)
# Sometimes, you don't know what is in the list, but you know
# you want to get rid of something at a specific index
food_list.pop(0)
print(food_list)
# Notice that "pizza" is no longer in the list because was is at index 0.

# Practice time...
"""
1. Make a new list with 3 items
2. Add a 4th item to the list
3. Remove one of the first three items from the list.
I'll come around and check progress/fix errors.
"""

# Finding things in a list
print(food_list.index("chicken"))
# This printed 9 for me, so chicken must be at index 9.
# This is an easy way of finding things in a list.

# Things I notice people do:
# Some people have made lists with parentheses instead of brackets
brands = ("apple", "samsung", "HTC")
# This is a TUPLE, not a list. Tuples are immutable (cannot be changed)

# Changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list1)

# Changing back into a string (list→string)
print("!".join(list1))