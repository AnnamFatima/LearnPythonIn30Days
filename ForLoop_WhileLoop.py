'''#Write a Python script that prints numbers from 1 to 10 using a for loop.

for i in range (1,11):
    print (i)

for i in range(11):
    print(i)'''

'''#Create a list of your favorite Python libraries and use a for loop to print each one.

libraries = ['NumPy' , 'Pandas' , 'Matplotlib ', 'Seaborn' , 'Requests' , 'Json' , 'Datetime' , 'Os']
for x in libraries:
    print(x)'''

'''#Write a program using a while loop to calculate the sum of numbers from 1 to 50.

sum=0
counter = 1
while counter <= 50:
    sum += counter
    counter = counter +1

print ( "the sum of numbers from 1 to 50: ",sum)

#With the For loop

sum = 0
for i in range (1,51):
    sum += i
    
print("the sum of numbers from 1 to 50: ",sum)
'''

'''#Find the First Divisible Number: 
# Write a loop to find the first number divisible by both 3 and 5 in a list,and use break to exit after finding it.

numbers = range (1,101)
for i in numbers:
    if i % 3 ==0 and i % 5 == 0:
        print("The first number divisible by both 3 and 5 is : ",i)
        break'''

'''#Skip Even Numbers: Write a loop that prints only odd numbers from 1 to 10 using continue.

numbers = range (11)
print("The odd numbers from 1 to 10 are : ")
for i in numbers:
    if i % 2==0 :
        continue
    print(i)'''

'''#Check Completion: Write a loop with an else block to check if a list of numbers has been fully iterated without a break.

numbers = range (1,101)
for i in numbers:
    if i %3 ==0 and i% 5 == 0:
        print("the first number divisible by both 3 and 5: ",i)
        break
else:
    print("Loop completed without a break")'''


'''numbers = range (1,101)
for i in numbers:
    if i %3 ==0 and i% 5 == 0 and i % 7 == 0:
        print("the first number divisible by both 3 ,5 and 7 is : ",i)
        break
else:
    print("Loop completed without a break")
        
    
'''
'''#Sum of a List: Write a Python program that calculates the sum of all numbers in a list using a for loop.

sum = 0
numbers = range (1,101)
print("The sum of all numbers from 1 to 100 is : ")
for i in numbers:
    sum += i
print(sum)
'''
'''
#Multiplication Table: Write a program that prints the multiplication table for any given number using a for loop.


def print_multiplication_table(n):
    print("Multiplication table for ",n)
    for i in range(1,11):     #for number from 1-10
        multiplication = n * i 
        print(f"{n} x {i} = {multiplication}")

#test the function
num = int(input("Enter the number: "))
print_multiplication_table(num)
'''

'''#Reverse a String: Use a for loop to reverse a given string
def reverse_string(s):
    reversed_s = ""
    for i in range(len(s) -1,-1,-1):
        reversed_s += s[i]
    return reversed_s

original_string = input("Enter a string: ")
reversed_string = reverse_string(original_string)
print("Reversed string: ", reversed_string)


# Factorial Calculation: Write a program to calculate the factorial of a number using a for loop.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test the function
num = int(input("Enter a number: "))
fact = factorial(num)
print(f"The factorial of {num} is {fact}")

'''

'''#Count Vowels: Write a program that counts the number of vowels in a given string using a for loop.

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Test the function
string = input("Enter a string: ")
vowel_count = count_vowels(string)
print(f"The number of vowels in '{string}' is {vowel_count}")'''


'''#While Loop Practice Questions:
#Guessing Game: Write a program where the user has to guess a number between 1 and 10. 
#The program should keep asking for a guess until the user gets it right using a while loop.

import random

#Generate a random number between 1 to 10
secret_number = random.randint(1,10)

print("Welcome to the guessing game.")
print("I'm thinking of a number between 1 and 10.")

while True:
    #ask the user for a guess 
    user_guess = int(input("Guess a number : "))
    #check if the user guess is correct
    if user_guess == secret_number:
        print(f"Congratulations! You guessed it ! The number was {secret_number}.")
        break
    elif user_guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too High! Try again.")

'''

'''#Sum of Digits: Write a program that calculates the sum of the digits of a given number using a while loop.

num = int(input("Enter a number: "))

sum_of_digits = 0
while num != 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10

print(f"The sum of digits is {sum_of_digits}")'''

'''#Fibonacci Sequence: Generate the first 10 numbers of the Fibonacci sequence using a while loop.

# Initialize the first two numbers of the Fibonacci sequence
a, b = 0, 1

# Initialize a counter to keep track of the number of terms generated
count = 0

# Initialize an empty list to store the Fibonacci sequence
fib_sequence = []

# Use a while loop to generate the first 10 numbers of the Fibonacci sequence
while count < 10:
    # Add the current number to the sequence
    fib_sequence.append(a)
    
    # Calculate the next number in the sequence
    a, b = b, a + b
    
    # Increment the counter
    count += 1

# Print the first 10 numbers of the Fibonacci sequence
print("The first 10 numbers of the Fibonacci sequence are:")
print(fib_sequence)
'''

'''#Collatz Sequence: Write a program that generates the Collatz sequence for any positive integer using a while loop.
def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Get the input from the user
num = int(input("Enter a positive integer: "))

# Generate and print the Collatz sequence
print("The Collatz sequence for", num, "is:")
print(collatz_sequence(num))'''

'''#Palindrome Checker: Use a while loop to check if a given string is a palindrome.

def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

# Get the input from the user
string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    '''

'''#Loop Control Statements Practice Questions:
#Prime Number Check: Write a program that checks if a number is prime. Use a for loop and break if the number is divisible 
# by any other number than 1 and itself.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        break
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")'''

'''#Sum Until Negative: Write a program that keeps asking the user to input numbers and adds them to a total sum until 
# a negative number is entered. Use a while loop with a break statement to exit when the negative number is input.

total_sum = 0

while True:
    num = float(input("Enter a number: "))
    if num < 0:
        break
    total_sum += num

print("The total sum is:", total_sum)
'''

'''#Skip Multiples of 3: Write a for loop that prints numbers from 1 to 20 but skips multiples of 3 using continue.

number  = range (1,21)
for i in number:
    if i % 3 == 0:
        continue
    print(i)
'''

'''#Search in a List: Write a program that searches for a specific value in a list. 
# If the value is found, print it and exit the loop using break. If not found, print "Not found" using the else block.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 7

for item in my_list:
    if item == target_value:
        print("Found:", item)
        break
else:
    print("Not found")'''


'''#Sum of Even Numbers: Write a program that sums even numbers from 1 to 50.
#  If the sum exceeds 200, use break to stop adding and print the current sum.


sum = 0
numbers = range(1, 51)
print("The sum of all even numbers from 1 to 50 is : ")

for i in numbers:
    if i % 2 == 0:  # check if i is even
        sum += i  # add i to the sum
    if sum > 200:
        break

print(sum)'''

'''#Nested Loops: Write a program that prints a pattern using nested for loops.
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()



for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end= " ")
    for k in range(i):
        print("* ", end= " ")
    print()'''


'''#Infinite Loop Break: Write a while loop that would run infinitely but include a break statement after a specific condition is met.
i = 0
while True:
    i += 1
    print(i)
    if i >= 10:
        break'''
        
