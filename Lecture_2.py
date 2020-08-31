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










