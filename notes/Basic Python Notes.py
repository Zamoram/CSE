"""
print("Hello World!")

# Apparently I'm going to slow, so I will speed up
# This is a comment
# This has no effect on the code
# This is used for a variety of things, such as
# 1.Making personal motes about my code
# 2.Commenting out code that does not work

print("Notice what is happening here.")
print()   # This creates a new line
print()   # Do you notice the underline here?
# Hover over top it to see what is wrong.

# Math
print(5 + 3)
print(5 - 3)
print(4 * 5)
print(6 / 5)
print()

# Semi-advanced math
print("Figure this out..")
print(6 // 4)
print(12 // 3)
print(9 // 4)   # This will ONLY give me a whole number
print()

print("Figure this out too...")
print(6 % 4)
print(5 % 3)
print(9 % 4)

# Defining Variables
car_name = "Wiebe mobile"  # String
car_type = "Tesla"  # String
car_cylinders = 16  # Integer
car_miles_per_gallon= 0.01  # Float

print("I have a car called %s. It's pretty nice." % car_name)
print("It has %d cylinders, but gets %f mpg" %(car_cylinders, car_miles_per_gallon))

# Taking Input
name = input("What is your name? ")
print("Hello %s" % name)

age = input("How old are you?")
print("%s? You belong in a museum!" %  age)

# Recasting
real_age = int(input("How old are you again?"))
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
    print (2*x + 3)


f(1)
f(5)
f(5000)


def distance(x1,y1, x2, y2 ):
    dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print(dist)


distance(0, 0, 3, 4)
distance(0, 0, 5, 12)
