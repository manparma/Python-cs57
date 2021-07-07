# Homework assignment 2

# Write the below programs with a while loop and a for loop:
# Sum the even numbers from 0 to 100 (inclusive)
# Sum the odd numbers from 0 to 100 (inclusive)
# Write a program that counts the vowels in this sentence.
# Asks a user to enter a temperature in celsius (via raw_input) and outputs the temperature in fahrenheit.
# Write a program that outputs the value of adding all numbers 1 to n.
# A user will input n via raw_input. Assume n is a positive integer greater than 1.
# For Example: n of 4, would result in 10 (1+2+3+4)

# Problem 1
# 1a) Sum the even numbers from 0 to 100 (inclusive) with a while loop

total = 0
number = 0
while (number < 100):
    number = number +2
    total = number + total
print("The sum of even numbers from 1 to 100 is", total)


# Problem 2
# 1a) Sum the even numbers from 0 to 100 (inclusive) with a for loop

total = 0
for number in range(2,102,2):
    total = number + total
print("The sum of even numbers from 1 to 100 is", total)


# Problem 3
# 1b) Sum the odd numbers from 0 to 100 (inclusive) with a while loop
total = 0
number = 1
while (number < 100):
    total = number + total
    number = 2 + number

print "The sum of odd numbers from 1 to 100 is", total

