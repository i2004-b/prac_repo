# January 21, 2025
# Lecture 3

# Lists
cart = ["apples", "bananas", "cherries"]
print(cart)

cart.append("donuts") # append can only take on argument
cart.append("eggs")
cart.append("flour")
print(cart)

cart.remove("cherries")
print(cart)

cart.append("donuts")
print(cart)

cart.remove("donuts") # Removes first instance
print(cart)

if "pineapple" in cart:
    cart.remove("pineapple") # Trying to remove something not in list produces error so check using if statement

donut_count = cart.count("donuts")
print(donut_count)

cart.pop(3)
print(cart)

cart.pop() # When nothing specified, removes last element
print(cart)
# Can visualize Python list as a stack using the .pop() method => LIFO

cart.reverse() # Reverse order
print(cart)

cart.sort()
print(cart) # Because it is string, it is alphabetical

cart.append("cherries")
cart.sort()

cart.append("bananas")
cart.append("grapes")
cart.append("oranges")
print(cart)

# Syntax for slicing: name_of_list[start_index : end_index]
fruit_basket = cart[4:] # or [-3:]
print(fruit_basket)

squares = []
for i in range(1, 10):
    squares.append(i * i)

print(squares)

# List comprehension -> compact, faster, and convenient way to produce a list
# List comp is faster under the hood than the previous for loop way
squares_new = [x * x for x in range(1, 10)] # for x in range 1 through 10, what is put into the list for each iteration is x * x
print(squares_new)

# List comprehension filter using an if
values = [34, 27, 95, 18, 36, 21, 64, 50, 77]
even_values = [x for x in values if x % 2 == 0]
print(even_values)

b_items = [i for i in cart if i.startswith("b")] # .startswith checks what letter a word begins with
print(b_items)

# Following two lines gives error (can add elements but can't add like this because list is empty) so declare list with default values
# inventory = []
# inventory[0] = 100

# To not get error, initialize list length
inventory = [0] * len(cart)
print(inventory)
inventory[0] = 100
print(inventory)

# Sets
# Empty set declaration:
number_set = set()

number_set = {1, 1, 2, 3, 4, 0, 10, 5} # Sets can't have duplicates. 
# The two 1s will not cause error, but when printing it out you will see that only one 1 has been added to set
# For sets, order is not guaranteed
print(number_set)

number_set.add(-10)
print(number_set)

# NOTE: Sets are slower, the order is not guaranteed, but NO duplicates

num_lst = [1, 1, 4, 5, 5, 6, 6]
no_dups = set(num_lst)
print(no_dups)
no_dups = list(no_dups) # Convert back to list
print(no_dups)

ns = sorted(number_set) # Returns value back as a LIST, but original set stays unchanged
print(ns)

# Dictionary: data structure used to map a set of keys to their values
# Uses of dictionary: 1. Look up values 2. Count occurrences 3. Store a record of related values
# Dictionary are also useful for counting frequencies (used in ML)

fav_snacks = {} # Declare empty dict
fav_snacks = {
    "kathleen": "tortilla chips",
    "maggie": "pretzels",
    "emily": "buffalo chicken dip",
    "ava": "chocolate",
}

print(fav_snacks)
fav_snacks["wade"] = "popcorn"
print(fav_snacks)

print("kathleen's favorite snack is " + fav_snacks["kathleen"])
# Below gives keyError because it does not exists, can use if statement to check
# print("bob's favorite snack is " + fav_snacks["bob"])

if "bob" in fav_snacks:
    print("bob's favorite snack is " + fav_snacks["bob"])

for key in fav_snacks: # by default, it returns key
    print(key + "'s favorite food is " + fav_snacks[key])
    # Putting in curly brackets is called escaping them
    print(f"{key}'s favorite food is {fav_snacks[key]}")

for key, value in fav_snacks.items(): # Get both key and value; similar to enumerate for lists
    print(key, value)

keys = fav_snacks.keys()
values = fav_snacks.values()

fav_snacks["alice"] =  ["chips", "nuts"]
print(fav_snacks)
# KEY CAN'T BE LIST; VALUE CAN BE ANYTHING
# No duplicate keys allowed, but duplicate values is good

