# AI & Python - Module 1
# Day 4 - Functions


# 1. Simple Function
def greet():
    print("Hello, Welcome to Python!")


greet()


# 2. Addition using Function
def add(a, b):
    return a + b


print("Addition:", add(10, 20))


# 3. Subtraction using Function
def subtract(a, b):
    return a - b


print("Subtraction:", subtract(20, 10))


# 4. Multiplication using Function
def multiply(a, b):
    return a * b


print("Multiplication:", multiply(10, 5))


# 5. Prime Number
def is_prime(n):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False


num = int(input("Enter a number to check prime: "))

if is_prime(num):
    print("Prime")
else:
    print("Not Prime")


# 6. Factorial
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


num = int(input("Enter a number for factorial: "))
print("Factorial:", factorial(num))


# 7. Fibonacci
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c


num = int(input("Enter number of Fibonacci terms: "))
fibonacci(num)


# 8. Sum of Digits
def sum_of_digits(n):
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10

    return total


num = int(input("Enter a number to find sum of digits: "))
print("Sum of digits:", sum_of_digits(num))
