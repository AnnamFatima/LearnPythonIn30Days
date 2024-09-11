# LearnPythonIn30Days
We are practicing python questions and learning basic python .
****** READ.ME FILE *******


#Write a program that takes an integer input from the user and checks if the number is even or odd.

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("The given number is an even number")
else:
    print("The given number is an odd number")

Explanation:

n / 2 will give you the result of the division, not the remainder. For example, if n is 5, n / 2 will be 2.5, not 1.
To check if a number is even or odd, you need to check the remainder of the division by 2. In Python, you can use the modulo operator % to get the remainder. So, n % 2 will give you the remainder of n divided by 2.
If the remainder is 0, the number is even. If the remainder is not 0, the number is odd.
Example use cases:

If the user enters 10, the output will be "The given number is an even number".
If the user enters 11, the output will be "The given number is an odd number".

#Grade Calculator:

#Write a program that takes a student's score as input and prints the grade based on the following criteria: #A: 90 and above #B: 80-89 #C: 70-79 #D: 60-69 #F: Below 60

score = int(input("Enter your marks: "))

if score >= 90: 
	print("Your Grade : A") 
elif 80 <= score <=89: 
	print("Your Grade : B") 
elif 70 <= score <= 79: 
	print("Your Grade : C") 
elif 60 <= score <= 69: 
	print("Your Grade : D") 
elif score < 60: 
	print("Your Grade : F")


 Here's a slightly more concise version:

score = int(input("Enter your marks: "))

if score >= 90:
    print("Your Grade : A")
elif score >= 80:
    print("Your Grade : B")
elif score >= 70:
    print("Your Grade : C")
elif score >= 60:
    print("Your Grade : D")
else:
    print("Your Grade : F")
Explanation:

The elif statements are evaluated in order, so you don't need to specify the upper bound for each range. For example, if the score is 85, it will be caught by the elif score >= 80: condition, so you don't need to specify elif 80 <= score <= 89:.
The else clause at the end will catch any scores below 60, so you don't need to specify elif score < 60:.
This code will work correctly for scores between 0 and 100. If the user enters a score outside this range, the program will still work, but the grade will be incorrect. If you want to add input validation to ensure the score is between 0 and 100, you can add an additional check:


score = int(input("Enter your marks: "))

if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
else:
    if score >= 90:
        print("Your Grade : A")
    elif score >= 80:
        print("Your Grade : B")
    elif score >= 70:
        print("Your Grade : C")
    elif score >= 60:
        print("Your Grade : D")
    else:
        print("Your Grade : F")



Number Comparison:

#Write a program that takes three numbers as input and prints the largest of the three.

n = int (input ( "Enter 1st number : " )) 
m = int (input ( "Enter 2nd number : " )) 
p = int (input ( "Enter 3rd number : " ))

print( max(n,m,p))




Here's a slightly more verbose version that uses conditional statements to find the largest number:


n = int(input("Enter 1st number: "))
m = int(input("Enter 2nd number: "))
p = int(input("Enter 3rd number: "))

if n >= m and n >= p:
    print("The largest number is:", n)
elif m >= n and m >= p:
    print("The largest number is:", m)
else:
    print("The largest number is:", p)

This code uses if-elif-else statements to compare the three numbers and print the largest one. However, the max() function is a more concise and efficient way to achieve the same result.

#Vowel or Consonant:

#Write a program that takes a character as input and checks if it is a vowel or a consonant.

Consider both uppercase and lowercase characters.


char = input("Enter a character: ")

if char.lower() in 'aeiou':
    print("The character is a vowel.")
elif char.isalpha():  # Check if the character is a letter
    print("The character is a consonant.")
else:
    print("The character is not a letter.")


Here's how the program works:

The input() function takes a character as input from the user.
The lower() method is used to convert the input character to lowercase, so that we can check for both uppercase and lowercase vowels.
The in operator is used to check if the character is in the string 'aeiou', which contains all the vowels.
If the character is a vowel, the program prints "The character is a vowel."
If the character is not a vowel, the program checks if it is a letter using the isalpha() method. If it is a letter, it must be a consonant, so the program prints "The character is a consonant."
If the character is not a letter, the program prints "The character is not a letter."


#Leap Year Checker:

#Write a program that takes a year as input and checks if it is a leap year. A year is a leap year if: 
#It is divisible by 4 
#If it is divisible by 100, it should also be divisible by 400

A year is considered a leap year if it meets certain conditions based on its divisibility by 4, 100, and 400. Here’s how it works mathematically:

Divisible by 4:

A year is a leap year if it is divisible by 4.
For example, 2024 ÷ 4 = 506, so 2024 is divisible by 4.
Not Divisible by 100:

However, if the year is also divisible by 100, it is not a leap year unless it meets the next condition.
For example, 1900 ÷ 100 = 19, so 1900 is divisible by 100 and not a leap year.
Divisible by 400:

If the year is divisible by 400, it is a leap year, even if it was divisible by 100.
For example, 2000 ÷ 400 = 5, so 2000 is divisible by 400 and is a leap year.
Summary:
A year is a leap year if:
It is divisible by 4 and (not divisible by 100 or divisible by 400).
Examples:
1600: Divisible by 4, 100, and 400 (Leap year)
1700: Divisible by 4 and 100, but not by 400 (Not a leap year)
2000: Divisible by 4, 100, and 400 (Leap year)
2024: Divisible by 4 but not by 100 (Leap year)
2100: Divisible by 4 and 100, but not by 400 (Not a leap year)


CODE:

year = int(input("Enter a year: "))

if year % 4 != 0:
    print("It is not a leap year.")
elif year % 100 != 0:
    print("It is a leap year.")
elif year % 400 != 0:
    print("It is not a leap year.")
else:
    print("It is a leap year.")

This code checks the following conditions:

If the year is not divisible by 4, it's not a leap year.
If the year is divisible by 4 but not by 100, it's a leap year.
If the year is divisible by 100 but not by 400, it's not a leap year.
If the year is divisible by 400, it's a leap year.

Here's a more concise version using a single conditional statement:

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")

This code uses the logical or operator to combine the two conditions for a leap year:

year % 4 == 0 and year % 100 != 0: The year is divisible by 4 but not by 100.
year % 400 == 0: The year is divisible by 400.
If either of these conditions is true, the year is a leap year. Otherwise, it's not a leap year.

Age Group:

Write a program that takes the age of a person as input and prints the age group:
Child: Below 12
Teenager: 13-19
Adult: 20-59
Senior: 60 and above

age = int(input("Enter your age : "))

if age < 12:
    print("You are a child.")
elif 12 < age <= 19:
    print("You are a Teenager.")
elif 19 < age <= 59:
    print("You are an Adult.")
else: 
    print("You are a Senior")

Explanation:

In the first condition, we use < 12 instead of <= 12 because 12 is already included in the teenager age group.
In the second condition, we use 12 < age <= 19 to specify that the age should be greater than 12 and less than or equal to 19.
Similarly, in the third condition, we use 19 < age <= 59 to specify that the age should be greater than 19 and less than or equal to 59.



Simple Calculator:

Write a program that takes two numbers and an operator (+, -, *, /) as input and performs the corresponding operation using if, elif, and else.




a = int(input("Enter the First number : "))
b = int(input("Enter the Second number : "))
operator = input("Enter the operator ('+','-','*','/'): ")

if operator == '+' :
    print(a + b)
elif operator == '-' :
    print(a - b)
elif operator == '*' :
    print(a * b)
elif operator == '/' :
    if b != 0:
        print(a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please enter one of the following: +, -, *, /")

You take two numbers a and b as input from the user.
You take an operator as input from the user.
You use an if-elif-else statement to perform the corresponding operation based on the operator:
If the operator is +, you add a and b.
If the operator is -, you subtract b from a.
If the operator is *, you multiply a and b.
If the operator is /, you divide a by b, but only if b is not zero. If b is zero, you print an error message.
If the operator is not one of the four basic arithmetic operators, you print an error message indicating that the operator is invalid.

Here's the same program with some minor improvements for better readability and user experience:

# Take input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

# Perform the operation based on the operator
if operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator: Please enter any one of the operators '+', '-', '*', '/'")

Bonus Challenge
Triangle Type Checker:
Write a program that takes the lengths of three sides of a triangle as input and determines if it is an equilateral, isosceles, or scalene triangle.


length1 = float(input("Enter the length of the first side: "))
length2 = float(input("Enter the length of the second side: "))
length3 = float(input("Enter the length of the third side: "))

if length1 == length2 == length3:
    print("The triangle is equilateral.")
elif length1 == length2 or length2 == length3 or length1 == length3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")

Explanation:

We first take the lengths of the three sides of the triangle as input from the user.
We then use an if-elif-else statement to determine the type of triangle:
If all three sides are equal, the triangle is equilateral.
If any two sides are equal, the triangle is isosceles.
If all three sides are different, the triangle is scalene.

LOOPS

'''#Write a Python script that prints numbers from 1 to 10 using a for loop.

for i in range (1,11):
    print (i)

for i in range(11):
    print(i)

Here's a breakdown of how it works:

The range(1, 11) function generates a sequence of numbers starting from 1 and ending at 10 (the upper limit is exclusive, so it stops at 10).
The for loop iterates over this sequence, assigning each number to the variable i in each iteration.
The print(i) statement prints the current value of i in each iteration.

'''#Create a list of your favorite Python libraries and use a for loop to print each one.

libraries = ['NumPy' , 'Pandas' , 'Matplotlib ', 'Seaborn' , 'Requests' , 'Json' , 'Datetime' , 'Os']
for x in libraries:
    print(x)

Here's a breakdown of how it works:

You define a list libraries containing the names of your favorite Python libraries as strings.
The for loop iterates over the libraries list, assigning each library name to the variable x in each iteration.
The print(x) statement prints the current value of x, which is the name of a library.

'''#Write a program using a while loop to calculate the sum of numbers from 1 to 50.

sum=0
counter = 1
while counter <= 50:
    sum += counter
    counter = counter +1

print ( "the sum of numbers from 1 to 50: ",sum)

Here's how the program works:

We initialize two variables: sum to store the sum of the numbers, and a counter.
The while loop continues to execute as long as counter is less than or equal to 50.
Inside the loop, we add the current value of counter to the sum variable.
We increment counter by 1 to move to the next number.
Once the loop finishes, we print the final value of sum, which is the sum of numbers from 1 to 50.

We can Also Use the FOR LOOP function for the same 

sum = 0
for i in range (1,51):
    sum += i
    
print("the sum of numbers from 1 to 50: ",sum)


Find the First Divisible Number: Write a loop to find the first number divisible by both 3 and 5 in a list, and use break to exit after finding it.

numbers = range(1, 101)
for i in numbers:
    if i % 3 == 0 and i % 5 == 0:
        print("The first number divisible by both 3 and 5 is:", i)
        break

We define a range of numbers from 1 to 100 using range(1, 101).
We iterate over this range using a for loop.
Inside the loop, we check if the current number i is divisible by both 3 and 5 using the modulo operator (%). If i is divisible by both, the remainder will be 0.
If we find a number that meets the condition, we print it and use the break statement to exit the loop. This ensures we only find the first number that meets the condition.



#Skip Even Numbers: Write a loop that prints only odd numbers from 1 to 10 using continue.

numbers = range(11)
print("The odd numbers from 1 to 10 are:")
for i in numbers:
    if i % 2 == 0:
        continue
    print(i)


The continue statement skips the print(i) for even numbers.
The print("The odd numbers from 1 to 10 are:") statement is outside the loop, so it only prints once before listing the odd numbers.


Check Completion: Write a loop with an else block to check if a list of numbers has been fully iterated without a break.

numbers = range(1, 101)
for i in numbers:
    if i % 3 == 0 and i % 5 == 0:
        print("The first number divisible by both 3 and 5: ", i)
        break
else:
    print("Loop completed without a break")


Now, the else block will only be executed if the loop completes without encountering a break statement.

However, in this specific case, the else block will never be executed, because the break statement will always be reached when the first number divisible by both 3 and 5 is found (which is 15).

If you want to demonstrate the else block being executed, you can modify the condition to something that will never be true, like this:



numbers = range(1, 101)
for i in numbers:
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        print("The first number divisible by 3, 5, and 7: ", i)
        break
else:
    print("Loop completed without a break")

In this case, the else block will be executed, because the loop will complete without finding a number that meets the condition.



PRACTICE QUESTIONS 

#Sum of a List: Write a Python program that calculates the sum of all numbers in a list using a for loop.

sum = 0
numbers = range (1,101)
print("The sum of all numbers from 1 to 100 is : ")
for i in numbers:
    sum += i
print(sum)

Your code is correct and will calculate the sum of all numbers from 1 to 100. However, there's a more concise way to do it using the built-in sum function in Python:

numbers = range(1, 101)
print("The sum of all numbers from 1 to 100 is :", sum(numbers))

This will achieve the same result with less code.

If you still want to use a for loop, your original code is correct. Just a minor suggestion: you can use a more descriptive variable name instead of sum, since sum is a built-in function in Python. Here's the modified code:

total = 0
numbers = range(1, 101)
print("The sum of all numbers from 1 to 100 is :")
for i in numbers:
    total += i
print(total)



Multiplication Table: Write a program that prints the multiplication table for any given number using a for loop.

number = int(input("Enter a number: "))

print("Multiplication table for", number)
for i in range(1, 11):
    multiplication = number * i
    print(f"{number} x {i} = {multiplication}")

Here's how the program works:

The user is prompted to enter a number, which is stored in the number variable.
The program prints a header indicating the multiplication table for the entered number.
The for loop iterates from 1 to 10 (inclusive).
Inside the loop, the program calculates the product of the entered number and the current iteration number i using the * operator.
The program prints the multiplication equation and result using an f-string.

Enter a number: 5
Multiplication table for 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

Reverse a String: Use a for loop to reverse a given string.
def reverse_string(s):
    reversed_s = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_s += s[i]
    return reversed_s

# Test the function
original_string = input("Enter a string: ")
reversed_string = reverse_string(original_string)
print("Reversed string:", reversed_string)

Here's how the program works:

The reverse_string function takes a string s as input.
The function initializes an empty string reversed_s that will store the reversed string.
The for loop iterates from the last character of the original string (at index len(s) - 1) to the first character (at index 0), decrementing the index by 1 in each iteration (-1 as the step value).
Inside the loop, the program adds each character of the original string to the reversed_s string, in reverse order.
The function returns the reversed string.
The user is prompted to enter a string, and the reverse_string function is called with the input string.
The program prints the original string and the reversed string.

Enter a string: hello
Reversed string: olleh


Factorial Calculation: Write a program to calculate the factorial of a number using a for loop.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test the function
num = int(input("Enter a number: "))
fact = factorial(num)
print(f"The factorial of {num} is {fact}")


Here's how the program works:

The factorial function takes an integer n as input.
The function initializes a variable result to 1, which will store the factorial result.
The for loop iterates from 1 to n (inclusive), incrementing the loop variable i by 1 in each iteration.
Inside the loop, the program multiplies the result variable by the current loop variable i. This is the key step in calculating the factorial.
The function returns the final result value, which is the factorial of n.
The user is prompted to enter a number, and the factorial function is called with the input number.
The program prints the input number and its factorial result.


Enter a number: 5
The factorial of 5 is 120

Count Vowels: Write a program that counts the number of vowels in a given string using a for loop.

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
print(f"The number of vowels in '{string}' is {vowel_count}")

The count_vowels function takes a string s as input.
The function defines a string vowels that contains all the vowels (both lowercase and uppercase).
The function initializes a variable count to 0, which will store the count of vowels.
The for loop iterates over each character char in the input string s.
Inside the loop, the program checks if the current character char is in the vowels string using the in operator. If it is, it increments the count variable by 1.
The function returns the final count value, which is the number of vowels in the input string.
The user is prompted to enter a string, and the count_vowels function is called with the input string.
The program prints the input string and the count of vowels.

While Loop Practice Questions:
Guessing Game: Write a program where the user has to guess a number between 1 and 10. The program should keep asking for a guess until the user gets it right using a while loop.

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 10.")

while True:
    # Ask the user for a guess
    user_guess = int(input("Guess a number: "))

    # Check if the user's guess is correct
    if user_guess == secret_number:
        print(f" Congratulations! You guessed it! The number was {secret_number}.")
        break
    elif user_guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

Here's how the program works:

The program generates a random number between 1 and 10 using the random.randint function and stores it in the secret_number variable.
The program prints a welcome message and explains the game to the user.
The program enters an infinite while loop, which will continue until the user guesses the correct number.
Inside the loop, the program asks the user for a guess using the input function and converts the input to an integer using the int function.
The program checks if the user's guess is correct by comparing it to the secret_number. If it is, the program prints a congratulatory message and exits the loop using the break statement.
If the user's guess is not correct, the program provides a hint by printing "Too low!" if the guess is less than the secret_number or "Too high!" if the guess is greater than the secret_number.
The loop continues until the user guesses the correct number.

Sum of Digits: Write a program that calculates the sum of the digits of a given number using a while loop.

num = int(input("Enter a number: "))

sum_of_digits = 0
while num != 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10

print(f"The sum of digits is {sum_of_digits}")

The program prompts the user to enter a number and stores it in num.
The program initializes a variable sum_of_digits to store the sum of digits, initialized to 0.
The program enters a while loop, which continues until num becomes 0.
Inside the loop, the program calculates the last digit of num using the modulo operator (%) and adds it to sum_of_digits.
The program then performs integer division on num by 10 using the floor division operator (//) to remove the last digit.
The loop continues until num becomes 0, at which point the sum of digits is stored in sum_of_digits.
The program prints the sum of digits using an f-string.

Fibonacci Sequence: Generate the first 10 numbers of the Fibonacci sequence using a while loop.

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

The program initializes the first two numbers of the Fibonacci sequence, a and b, to 0 and 1, respectively.
The program initializes a counter, count, to keep track of the number of terms generated.
The program initializes an empty list, fib_sequence, to store the Fibonacci sequence.
The program enters a while loop, which continues until count reaches 10.
Inside the loop, the program adds the current number, a, to the fib_sequence list.
The program calculates the next number in the sequence by swapping the values of a and b and adding the previous value of a to b.
The program increments the count variable.
The loop continues until count reaches 10, at which point the program prints the first 10 numbers of the Fibonacci sequence.

Collatz Sequence: Write a program that generates the Collatz sequence for any positive integer using a while loop.

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
print(collatz_sequence(num))

Here's how the program works:

The program defines a function collatz_sequence that takes a positive integer n as input.
The function initializes an empty list sequence to store the Collatz sequence.
The function enters a while loop, which continues until n reaches 1.
Inside the loop, the program checks whether n is even (i.e., n % 2 == 0).
If n is even, the program divides n by 2 using integer division (//).
If n is odd, the program multiplies n by 3 and adds 1.
The program appends the new value of n to the sequence list.
The loop continues until n reaches 1.
The function returns the sequence list.
The program gets an input from the user and passes it to the collatz_sequence function.
The program prints the Collatz sequence for the input number.



Palindrome Checker: Use a while loop to check if a given string is a palindrome.

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

The program defines a function is_palindrome that takes a string s as input.
The function initializes two indices, i and j, to the start and end of the string, respectively.
The function enters a while loop, which continues until i meets or exceeds j.
Inside the loop, the program checks whether the characters at indices i and j are equal.
If the characters are not equal, the function returns False, indicating that the string is not a palindrome.
If the characters are equal, the program increments i and decrements j to move towards the center of the string.
The loop continues until i meets or exceeds j.
If the loop completes without finding any unequal characters, the function returns True, indicating that the string is a palindrome.
The program gets an input from the user and passes it to the is_palindrome function.
The program prints whether the string is a palindrome or not.


Loop Control Statements Practice Questions:
Prime Number Check: Write a program that checks if a number is prime. Use a for loop and break if the number is divisible by any other number than 1 and itself.

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
    print(num, "is not a prime number.")

The is_prime function takes an integer n as input and returns True if it's prime, and False otherwise.
The function first checks if n is less than or equal to 1, in which case it's not prime.
The function then uses a for loop to iterate from 2 to the square root of n (inclusive). This is an optimization, as any factor larger than the square root would have a corresponding factor smaller than the square root.
Inside the loop, the function checks if n is divisible by i using the modulo operator (%). If it is, the function returns False, indicating that n is not prime.
If the loop completes without finding any divisors, the function returns True, indicating that n is prime.
The main loop iterates over the range of numbers from 0 to 100, and for each number, it calls the is_prime function. If the function returns True, the number is printed.

Sum Until Negative: Write a program that keeps asking the user to input numbers and adds them to a total sum until a negative number is entered. Use a while loop with a break statement to exit when the negative number is input.


total_sum = 0

while True:
    num = float(input("Enter a number: "))
    if num < 0:
        break
    total_sum += num

print("The total sum is:", total_sum)

The program initializes a variable total_sum to 0, which will store the sum of the input numbers.
The program enters an infinite loop using while True.
Inside the loop, the program prompts the user to enter a number using input.
The program checks if the input number is less than 0 using the if statement. If it is, the program executes the break statement, which exits the loop.
If the input number is not negative, the program adds it to the total_sum using the += operator.
The loop continues until a negative number is entered, at which point the program exits the loop.
Finally, the program prints the total sum using print.


Skip Multiples of 3: Write a for loop that prints numbers from 1 to 20 but skips multiples of 3 using continue.

number = range(1, 21)
for i in number:
    if i % 3 == 0:
        continue
    print(i)

The range(1, 21) function generates a sequence of numbers from 1 to 20.
The for loop iterates over this sequence, assigning each number to the variable i.
Inside the loop, the if statement checks if i is a multiple of 3 by using the modulo operator %. If i is a multiple of 3, the remainder of dividing i by 3 is 0.
If i is a multiple of 3, the continue statement is executed, which skips the rest of the loop body and moves on to the next iteration.
If i is not a multiple of 3, the print(i) statement is executed, printing the value of i.


Search in a List: Write a program that searches for a specific value in a list. If the value is found, print it and exit the loop using break. If not found, print "Not found" using the else block.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 7

for item in my_list:
    if item == target_value:
        print("Found:", item)
        break
else:
    print("Not found")

Here's how the program works:

The program defines a list my_list containing the values to search.
The program defines a target_value variable that specifies the value to search for.
The program uses a for loop to iterate over the my_list.
Inside the loop, the program checks if the current item is equal to the target_value using the if statement.
If the item matches the target_value, the program prints a success message and exits the loop using the break statement.
If the loop completes without finding the target_value, the else block is executed, printing "Not found".
Note that the else block is attached to the for loop, not the if statement. This is a special syntax in Python that allows you to specify a block of code to execute if the loop completes without encountering a break statement.

You can try running this program with different values for target_value to see how it works!


Sum of Even Numbers: Write a program that sums even numbers from 1 to 50. If the sum exceeds 200, use break to stop adding and print the current sum.

sum = 0
numbers = range(1, 51)
print("The sum of all even numbers from 1 to 50 is : ")

for i in numbers:
    if i % 2 == 0:  # check if i is even
        sum += i  # add i to the sum
    if sum > 200:
        break

print(sum)

I added an if statement to check if i is even using the modulo operator %. If i is even, the expression i % 2 == 0 evaluates to True.
Inside the if block, I add the even number i to the sum variable.
The rest of the code remains the same.
With this corrected code, the program should sum up the even numbers from 1 to 50 and stop adding when the sum exceeds 200.

Note that the sum of all even numbers from 1 to 50 is actually 650, so the program will stop adding at some point before reaching the end of the range.


Bonus Challenges:Nested Loops: Write a program that prints a pattern using nested for loops.

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

*
* *
* * *
* * * *
* * * * *

The outer for loop iterates from 1 to 5 (using range(1, 6)).
The inner for loop iterates from 0 to i-1 (using range(i)).
Inside the inner loop, the program prints a * character followed by a space (using print("*", end=" ")).
After the inner loop completes, the program prints a newline character (using print()).
The outer loop repeats the process, incrementing the number of * characters printed on each line.
You can modify the range and the pattern to create different patterns. For example, to print a pyramid pattern, you can use:

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")
    for k in range(i):
        print("* ", end=" ")
    print()

    * 
   * * 
  * * * 
 * * * * 
* * * * * 


Infinite Loop Break: Write a while loop that would run infinitely but include a break statement after a specific condition is met.
i = 0
while True:
    i += 1
    print(i)
    if i >= 10:
        break

The while True statement creates an infinite loop that will continue to run until a break statement is encountered.
The loop increments the value of i by 1 on each iteration.
The loop prints the current value of i.
The if statement checks if the value of i is greater than or equal to 10. If it is, the break statement is executed, which exits the loop.
When you run this code, you'll see the numbers 1 through 10 printed, and then the loop will stop.

Note that if you remove the if statement and the break statement, the loop will indeed run infinitely, printing numbers indefinitely.


******Functions And Modules *****

Functions in Python
What is a function?
A function is a block of reusable code that is used to perform a specific action. Functions allow you to write clean and maintainable code.

Syntax:

def function_name(parameters):
    # code block
    return result

Example:

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!


Key Concepts:
Defining a Function: You use the def keyword followed by the function name and parentheses.
Arguments/Parameters: Values you pass into the function to work with.
Return Statement: Used to send back a value from a function.
Default Parameters:


You can define default values for parameters.


def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!
print(greet("Bob"))  # Output: Hello, Bob!


Functions with Multiple Parameters:

def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8


Returning Multiple Values:
A function can return multiple values in the form of a tuple.


def get_values():
    return 1, 2, 3

x, y, z = get_values()
print(x, y, z)  # Output: 1 2 3


Some Examples:

Simple Greeting Function
Create a function that takes a name as input and prints a personalized greeting message.

def greet(name):
    print(f"Hello, {name}!")

greet("Annam")

2. Function to Add Two Numbers
#Write a function that takes two numbers as arguments and returns their sum.

def add(a,b):
    return(a+b)

result= add(8,9)
print(result)

 #Find the Maximum of Three Numbers
#Create a function that takes three numbers and returns the largest of them.
def numbers(x, y, z):
    return max(x, y, z)

result = numbers(141, 231, 789)
print(result)

Factorial Function #Write a function that calculates the factorial of a given number.def 

factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)
This function uses recursion to calculate the factorial of a given number n. Here's a breakdown of how it works:

The function checks if n is 0, in which case it returns 1 (since the factorial of 0 is defined to be 1).
If n is not 0, the function calls itself with n-1 as an argument, and multiplies the result by n. This process continues until n reaches 0.
The final result is the product of all the numbers from n down to 1, which is the definition of the factorial.
For example, if we call the function with n=5, it will calculate the factorial as follows:

factorial(5) = 5 * factorial(4)
             = 5 * (4 * factorial(3))
             = 5 * (4 * (3 * factorial(2)))
             = 5 * (4 * (3 * (2 * factorial(1))))
             = 5 * (4 * (3 * (2 * 1)))
             = 120

The output of the code will be 120, which is the correct factorial of 5.

Alternatively, you can also implement the factorial function using a loop instead of recursion:

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

result = factorial(5)
print(result)

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

result = factorial(5)
print(result)

#Task
#2 nos' if you add then you get 7
#square of the number's
#1functions call to be used 

def add(x ,y):
    return(x + y)
def square(z):
    return(z*z)

result = square(add(6,1))
print(result)
'''

'''#Factorial

def factorial(n):
    if n <2:
        return 1
    else:
        return n * (factorial(n-1))

result = factorial(4) 
print (result)'''

'''#Practice Exercise:
#Create a Simple Function: Write a function that takes a name as input and returns a personalized greeting.

def greet(name, greeting = "Hello"):
    return (f"{greeting} {name}!")

print(greet("Annam"))'''

#Function with Multiple Arguments: Create a function that calculates the area of a rectangle.

def area (length, width):
    return length * width
length = 8
width = 7

result = area (length , width)
print(f"Area of a rectangle : {result}")

Using Default Arguments: Write a function to print a list of items, with a default separator.

To create a function that prints a list of items with a default separator, you can define a function that takes a list of items and an optional separator as inputs. Here's an example of how you can do this:

def print_list(items, separator=', '):
    print(separator.join(map(str, items)))

# Example usage:
fruits = ['apple', 'banana', 'cherry']
print_list(fruits)  # Output: apple, banana, cherry

numbers = [1, 2, 3, 4, 5]
print_list(numbers, ' | ')  # Output: 1 | 2 | 3 | 4 | 5

In this example, the print_list function takes a list of items as the first argument, and an optional separator as the second argument. The default separator is a comma followed by a space (', '). The function uses the join method to concatenate the items in the list with the separator, and then prints the resulting string.

By using a default argument, you can call the function with just the list of items, and it will use the default separator. If you want to use a different separator, you can pass it as the second argument.

Note that I used the map function to convert each item in the list to a string, in case the list contains non-string items. This ensures that the join method works correctly.

Explore Variable Scope: Experiment with local and global variables inside and outside functions.

In Python, variables can be classified into two categories: local variables and global variables.

Local Variables: Local variables are those that are defined inside a function. They are only accessible within the function where they are defined and cannot be accessed from outside the function. Here's an example:

def my_function():
    local_var = 5  # Local variable
    print(local_var)  # Accessible here

my_function()
print(local_var)  # Raises an error because local_var is not accessible here

Global Variables: Global variables, on the other hand, are those that are defined outside any function. They are accessible throughout the program, including inside and outside functions. Here's an example:

global_var = 10  # Global variable

def my_function():
    print(global_var)  # Accessible here

my_function()
print(global_var)  # Accessible here

Modifying Global Variables: If you want to modify a global variable inside a function, you need to use the global keyword to indicate that the variable is global. Here's an example:

global_var = 10  # Global variable

def my_function():
    global global_var
    global_var = 20  # Modify the global variable
    print(global_var)  # Output: 20

my_function()
print(global_var)  # Output: 20

Nonlocal Variables: In Python, there's also a third category of variables called nonlocal variables. Nonlocal variables are used in nested functions, where a variable is defined in an outer function and accessed in an inner function. Here's an example:

def outer_function():
    nonlocal_var = 5  # Nonlocal variable

    def inner_function():
        nonlocal nonlocal_var
        nonlocal_var = 10  # Modify the nonlocal variable
        print(nonlocal_var)  # Output: 10

    inner_function()
    print(nonlocal_var)  # Output: 10

outer_function()

In this example, the nonlocal_var is defined in the outer_function and accessed in the inner_function. The nonlocal keyword is used to indicate that the variable is nonlocal.

