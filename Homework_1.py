# Homework assignment 1

#   1. Evaluate ((True and False) and True) or (True and False) or (True or True)
print ((True and False) and True) or (True and False) or (True or True)  # True

#  2. If a = catsanddogs what would the following evaluate to:
a = 'catsanddogs'
# a[3:9]
# a[2:]
# a[-3]

print(a[3:9])  # sanddo
print(a[2:])  # tsanddogs
print(a[-3])  # o

#  3. Asks a user to enter a word (via raw_input) and outputs the length of the word.
name = raw_input("My name is: ")
print ("Your name is", name, " and contains ", len(name), " letters.")
# print(len(name)) # another way


# 4. Asks a user to enter a number (via raw_input) and outputs the cube of that number.
# a. For example, input 5 would result in output of 125
number = (int(raw_input('Enter a number: ')))   # use int to specify for Integers types
print(number ** 3)


# 5. Asks a user to enter a radius (via raw_input) and outputs the area of a circle with the associated radius.
radius = (float(raw_input('Enter a radius: ')))  # use float to specify for types
pi = 3.14159
area = (pi * radius * radius)
print(area)
