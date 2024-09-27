'''#1. Simple Greeting Function
#Create a function that takes a name as input and prints a personalized greeting message.

def greet(name):
    print(f"Hello, {name}!")

greet("Annam")'''

'''#2. Function to Add Two Numbers
#Write a function that takes two numbers as arguments and returns their sum.

def add(a,b):
    return(a+b)

result= add(8,9)
print(result)'''

''' #Find the Maximum of Three Numbers
#Create a function that takes three numbers and returns the largest of them.
def numbers(x, y, z):
    return max(x, y, z)

result = numbers(141, 231, 789)
print(result)'''


'''#Factorial Function
#Write a function that calculates the factorial of a given number.

def factorial(n):
    if n==0:
        return 1
    else :
        return n * factorial(n - 1)
result = factorial(5)
print(result)'''

'''#Check for Prime Number
#Create a function that checks if a given number is prime.

def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True

result = is_prime(7)
print(result)'''

'''#Task
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

'''#Function with Multiple Arguments: Create a function that calculates the area of a rectangle.

def area (lenght, width):
    return length * width
length = 8
width = 7

result = area (length , width)
print(f"Area of a rectangle : {result}")'''

'''#Using Default Arguments: Write a function to print a list of items, with a default separator.

def print_list(items, separator=', '):
    print(separator.join(map(str, items)))

# Example usage:
fruits = ['apple', 'banana', 'cherry']
print_list(fruits)  # Output: apple, banana, cherry

numbers = [1, 2, 3, 4, 5]
print_list(numbers, ' | ')  # Output: 1 | 2 | 3 | 4 | 5'''

'''#Write a function greet_user(name) that takes a name as input and prints a personalized greeting message.

def greet_user(name):
    print(f"Hello, {name}!. Its nice meeting you.")
greet_user("Annam")'''

'''#Create a function add_numbers(a, b=5) that takes two arguments and returns their sum. 
#If the second argument is not provided, use 5 as the default value.

def add_numbers(a,b=5):
    return(a + b)

result = add_numbers(10)
print(result)'''

'''#Write a Python function factorial(n) that returns the factorial of a number using recursion.

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))
result= factorial(10)
print(result)'''

'''#Implement a function is_palindrome(word) that checks if a given word is a palindrome.

def is_palindrome(word):
    """
    Returns True if the given word is a palindrome, False otherwise.
    """
    # Convert the word to lowercase to ignore case sensitivity
    word = word.lower()
    
    # Compare the word with its reverse
    return word == word[::-1]

# Test the function with some examples
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False '''

def reverse_string(s):
    reversed_s = ""
    for i in range (len(s) -1,-1,-1):
        reversed_s += s[i]
    return reversed_s

original_string = input("Enter a string: ")
reversed_string = reverse_string(original_string)
print ("Reversed string: ", reversed_string)