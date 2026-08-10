# AI & Python - Module 1
# Day 2 - Python Basics


# 1. Variables
name = "Arnesh"
age = 19
mark = 85.5

print("Name:", name)
print("Age:", age)
print("Mark:", mark)


# 2. Data Types
a = 10
b = 10.5
c = "Python"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))


# 3. Input and Output
name = input("Enter your name: ")
print("Hello", name)


# 4. Arithmetic Operators
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# 5. Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 6. Positive or Negative
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 7. Largest of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)
