# AI & Python - Module 1
# Day 3 - Loops and Lists


# 1. Print numbers from 1 to 10
print("Numbers from 1 to 10:")

for i in range(1, 11):
    print(i)


# 2. Print numbers from 1 to 100
print("\nNumbers from 1 to 100:")

for i in range(1, 101):
    print(i)


# 3. Print even numbers from 1 to 50
print("\nEven numbers:")

for i in range(1, 51):
    if i % 2 == 0:
        print(i)


# 4. Print odd numbers from 1 to 50
print("\nOdd numbers:")

for i in range(1, 51):
    if i % 2 != 0:
        print(i)


# 5. Sum of numbers from 1 to 100
sum = 0

for i in range(1, 101):
    sum += i

print("\nSum from 1 to 100:", sum)


# 6. Multiplication table
num = int(input("\nEnter a number for multiplication table: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# 7. Create and print a list
numbers = [10, 20, 30, 40, 50]

print("\nList:")
print(numbers)


# 8. Print list elements
print("\nList elements:")

for x in numbers:
    print(x)


# 9. Sum of list elements
sum = 0

for x in numbers:
    sum += x

print("\nSum of list:", sum)


# 10. Find largest element
largest = numbers[0]

for x in numbers:
    if x > largest:
        largest = x

print("Largest element:", largest)


# 11. Find smallest element
smallest = numbers[0]

for x in numbers:
    if x < smallest:
        smallest = x

print("Smallest element:", smallest)
