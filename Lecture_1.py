from pip._vendor.distlib.compat import raw_input

#   defining variable name
x = 5
y = 9

#   multiply both variables and print
print (y*x)  # 45

#   <type 'int'> Integers
print(type(4))
print(type(x))
print(type(y))
print(type(x/y))

print(1+1)      # 2
print(1+1.0)    # 2.0
print(1.0+1.0)  # 2.0
print(2*2)      # 4
print(2*2.0)    # 4.0
print(3/2)      # 1
print(3/2.0)    # 1.5
print(type(3/2.0))    # 1.5 <type 'float'>
print(type((2+2)*3.0))    # 12.0 <type 'float'>
print (1+1,1+1.0,1.0+1.0,2*2,2*.0,3/2,3/2.0,(2+2)*3.0)  # (2, 2.0, 2.0, 4, 0.0, 1, 1.5, 12.0)

#   Strings
my_name = 'MF Doom'
age = 99
print(my_name)
print(age)


#   Introduction to bools
5 > 4   # True
5 >= 4  # True
3 < 3   # False
3 <= 3  # True
2 == 2.0    # True


#   Lecture 1 Examples

# 1
1 + 2 * 3  # 7 (int)

# 2
1 * 2 * 3.0  # 6.0 (float)

# 3
- - 5.0  # 5.0 (float)

# 4
4 / 8  # 0 (int)

# 5
4 < 5  # True (bool)

# 6
True and False  # False (bool)

# 7
(True and True) or False  # True (bool)

# 8
(2>3 or 2<3) and 3>4  # False (bool)


#   Variables
# since we can assign 'x' to an integer we can do the same with named variables

# EXAMPLES
apple = 10  # assing 10 to apple
banana = apple  # assign banana to apple
apple = 5  # assign 5 to apple
print (banana)
print (apple)

pi = 3.14159
radius = 5

area = pi * radius * radius
print(area)

# Knowledge Check slide - 89
x = 2
x + 3.0  # 5.0 (float)

x = x + 1.0  # 3.0 (float)

# Strings
a = "abc"
b = "hello"

print(a*2)
print(b+'3')

#   Built in operators
# len:
a = "losangeles"
print(len(a))

# indexing:
print(a[0])
print(a[3])
print(a[-1])

# slicing (substring):
print(a[1:3])   # 3-1=2 tells you length
print(a[5:9])

# My first Hello World Program: Hello World!
print('Hello World!')

# My second program: area of a rectangle
s1 = 2
s2 = 3
area = s1*s2
print(area)

