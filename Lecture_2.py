# Lecture 2

# A note on shorthand notation w/ primitives

x = 5
x += 12
print(x)    # 17

y = 11
y -= 4
print(y)    # 7

z = 3
z *= 5
print(z)    # 15

w = 8
w /= 2
print (w)   # 4

# Intro to Lists
# A list is a fundamental data structure.
# In the same way that we can instantiate a variable (like x = 4), we can instantiate a list.

a = [5, 10, 2, 4, 4]
print (a)   # [5, 10, 2, 4, 4]
print (a[2])    # 2 (from the list in line 25)

# Lists (re-referencing)
# You can also rename parts of an array by re-referencing.
b = [1, 2, 3, 4, 5]
print(b[2])     # 3
b[2] = 6
print(b)    # [1, 2, 6, 4, 5]
print(b[2])     # 6

# Lists (sub-lists)
# Extract substrings of a list

c = [0,1,2,3,4]
c[0] = 8
print (c)   # [8, 1, 2, 3, 4]

print(a[0])     # 5
print(a[0:2])   # [5, 10]
print(a[:2])    # [5, 10]
print(a[2:4])   # [2, 4]


# Introduction to the Range function
# Range is used to create lists of integers

print(list(range(4)))       # [0, 1, 2, 3]
print(list(range(4, 8)))     # [4, 5, 6, 7]
print(list(range(1, 13, 2)))  # [1, 3, 5, 7, 9, 11]


# Introduction to the While Loop
# while loop continues on infinitely until the loop is broken (evaluates to false)

count = 10
while (count != 0):
    print(count)
    count -= 1
print("Blastoff!")

# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Blastoff!


count = 3
while (count != 0):
    count -= 1
print(count)
print("Blastoff!")

# 0
# Blastoff!

# More While Loops

x = 3
while x > 0:
    print(x)
    x = x - 1


x = 10
while x > 3:
    print(x)
    x = x - 2
print("Way to go!")


# Introduction to For Loop
# The for loop has a specified range (or number of loops) and iterates over items of a sequence (like a list or a string)


# Range
for x in [0,1,2,3]:
    print(x)

for x in range(4):
    print(x)

i = 1
while (i<6):
    print(i)
    i+=1

for i in [1,2,3,4,5]:
    print(i)

for i in range(1,6):
    print(i)

# Branching
# Branching the if, elif, and else clauses


# Introduction to conditions via if/else:
name = str(raw_input("What is your name?"))
x = int(raw_input("What is 2+2?: "))
if x == 4:
    print("Nice work!", [name])
else:
    print("Try again!", [name])


name = str(raw_input("What is your name?"))
x = int(raw_input("What is 2+2?: "))
if x == 4:
    print("Nice work!", [name])
elif (x == 3) or (x == 5):
    print("So close!", [name])
else:
    print("Try again!", [name])

x = 100
if (x > 1):
    print("x is greater than 1!")
elif (x > 10):
    print("x is greater than 10!")
else:
    print("x is greater than 100!")

# Output !
x = 2
x + 5
if (x == 7):
    print "hello"
elif (x == 8):
    print "goodbye"
else:
    print "!"

# Output blue
y = 2
y = y + 2
if (y == 4):
    print "blue"
elif (y == 4):
    print "purple"
else:
    print "!"


