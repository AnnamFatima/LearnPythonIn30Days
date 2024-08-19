'''
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
'''
'''
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


'''

'''
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

'''

'''
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

'''

'''
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
'''

'''
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

'''

'''
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
'''

'''
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

'''