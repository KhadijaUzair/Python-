# Question 1: Write a Python program that asks the user for their name, age, city, and favorite programming language.
#  Then print their information and calculate how old they will be after 5 years.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
lang = input("Enter your favourite programming language: ")
print("\nYour name is: ",name)
print("Your age is: ",age)
print("Your city is: ",city)
print("Your favourite programming language is: ",lang)
age1 = age + 5
print("Your age after 5 years will be: ",age1)


# Question 2: Write a Python program that takes two numbers as input and prints their sum, difference, product, and division.

print("Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2
print("the sum of two numbers is",add)
print("the difference of two numbers is",subtract)
print("the product of two numbers is",multiply)
print("the division of two numbers is",divide)

