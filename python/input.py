name = input("Please enter your name: ") # If you give no input, looks like it is blank in terminal (but does work)
# Any time you read in input, it is treated as a string
print("Hello, " + name)

try:
    num = int(input("Enter a number: "))
    print(num)
    double = num * 2
    print(double)
except:
    print("You didn't enter a number")

# splitting only after second space??
# Opening file
with open("movies.txt") as file: # reads in movies and stores it in the object file
    # Double new line because of prnt statement and the newline from the og file so adjusted printed line
    for line in file:
        line = line.strip()
        print(line)


with open("heights.txt") as file:
    for line in file:
        info = line.strip().split() # Info will look like ["first", "last", "height"]
        print(info)

        info[2] = int(info[2])
        print(info)

file_name = input("Enter file name: ")
with open(file_name) as file:
    count = 1
    for line in file: # you could use enumerate instead of a counter
        print(f"{count}. {line.strip()}")
        count += 1
