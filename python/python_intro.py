# FIRST 2 LECTURES
# January 14, 2025
# Lecture 1
print("Hello World!")
# This is a comment
"""
This is a multi-line comment
"""

# To do the following, do command and /
# To negate it, do the same thing
# // this is a comment
# /*
# this is a line comment
# */

x = 100 # Declaring variable; this variale can hold a different data type later on
x = "hello"
x = [1, 2, 3] # At run time, it determines the type of the variable

print(x)

x = 100
y = 10
result = x / y # this will create a float, regardless
# To ignore the float conversion, you can use the floor function which will keep as an integer
result1 = x // y # doesn't round up, just cuts off decimal numbers
# Can also convert result to an integer
result2 = int(x / y)
print(result)
print(result1)
print(result2)

min_value = min(1, 2, 3)
print(min_value)
raised = pow(2, 3)
print(raised)
raised2 = 2 ** 3
print(raised2)
# Naming convention is snake_case


# If-statements
a = -1
b = 0

if a < 0:
    print("a is negative")
    b += 1
elif a > 0:
    print("a is positive")
else:
    print("a is zero")

x = 12
start = 10
end = 100
if x > start and x < end:
    print("x is within range")

if x < start or x > end:
    print("x is not in range")

# January 16, 2025
# Lecture 2
count = 0
while count < 5:
    print(count)
    count += 1 # Cntrl C kills application if infinite loop
    # CAN'T DO ++

for i in range(5):
    print(i, end=" ") # Now, only prints a space instead of newline
print() # Need to print the newline, now

for i in range(1, 15, 2): # Default for third spot is 1
    print(i, end=" ")
print()

lst = [2, 4, 6, 8]
for i in range(len(lst)):
    print(i, lst[i])

for val in lst:
    print(val, end=" ")
print()

for i, val in enumerate(lst): # Puts index place in i and the element value in val
    print(i, val)

# IN CLASS EXERCISE
# Exercise 1
for i in range(1, 21):
    if i % 3 == 0:
        print(i)

# Exercise 2 # You could just due counter +=2 which would save space
counter = 1
sum = 0
while counter <= 50:
    if counter % 2 == 0:
        sum += counter
    counter += 1

print(sum)

# Exercise 3
numbers = [5, 8, 2, 15, 10, 3, 7]
for i in range(len(numbers)):
    if numbers[i] > 5:
        print(numbers[i])

# Exercise 4
"""
list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 6, 10, 15]
"""

list1 = [1, 2, 3, 4, 5]

list2 = []

# running_sum = 0
# for i in range(len(list1)):
#     running_sum += list1[i]
#     list2.append(running_sum)
list2.append(list1[0])
for i in range(1, len(list1)):
    list2.append(list1[i] + list2[i - 1])

print(list2)

def hello_world():
    print("Hello World!")

hello_world()

def hello(name):
    print("Hello " + name)

hello("Ivan")

def hello2(name="Bob"):
    print("Hello " + name)

hello2()
hello2("Ivan")

# Exercise #1 - Swap Elements
def swap(list):
    tmp = list[0]
    list[0] = list[-1]
    list[-1] = tmp

new_list = [0, 3, 8, 4, 5]
swap(new_list)
print(new_list)

hello = "hello" # list of characters
for c in hello:
    print(c)

# Need to convert number to a string to concatenate it with a string
# E.g.:
subtotal = 14.75
sub_statement = "The subtotal is " + str(subtotal)
print(sub_statement)

# Can use * as a repetition operator
print("Ivan" * 7)
names = 15 * "Ivan"
print(names)

course = "Platform Computing"
# String slicing takes string name and give the index places that we want
# string[start:end]
plat = course[0 : 8]
plat_same = course[:8] # Does the same thing as above
# Can use .find() to find index place if you don't know the index
comp = course[9 : 18]
comp_same = course[9:]
print(comp)
print(comp_same)