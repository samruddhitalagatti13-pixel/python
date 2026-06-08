print("1. Write a function to check whether a number is positive, negative, or zero. ")
def Number(num):
    if num>=0:
        print("no. is positive")
    elif num<=0:
        print("no. is negative")
    else:
        print("not a valid no. / zero")

num = int(input("enter a no.:"))
Number(num)

print("2. Write a function to check whether a number is even or odd. ")
def Number(num):
    if num%2==0:
        print("no. is even")
    elif num%2!=0:
        print("no. is odd")
    else:
        print("not a valid no.")

num = int(input("enter a no.:"))
Number(num)

print("3. Write a function that accepts two numbers and returns the greater number. ")
def Number(num1, num2):
    if num1>num2:
        print("num1 is greater")
    elif num2>num1:
        print("num2 is greater")
    else:
        print("both are equal")

num1 = int(input("enter 1st no.:"))
num2 = int(input("enter 2st no.:"))
Number(num1, num2)

def Voting(age):
    if age>=18:
        print("eligible to vote")
    else:
        print("not eligible to vote")

age = int(input("Enter ur age:"))
Voting(age)

def Number(num):
    if num % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")

num = int(input("Enter a number: "))
Number(num)

def Year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

year = int(input("Enter year: "))
Year(year)

def Vowel(ch):
    if ch in 'aeiouAEIOU':
        print("is a vowel")
    else:
        print("is a consonent")

ch = input("Enter a character:")
Vowel(ch)

def Number(num1, num2, num3):
    if num1>num2 and num1>num3:
        print("num1 is greater")
    elif num2>num1 and num2>num3:
        print("num2 is greater")
    elif num3>num1 and num3>num2:
        print("num3 id greater")
    else:
        print("all are equal")

num1 = int(input("enter 1st no.:"))
num2 = int(input("enter 2st no.:"))
num3 = int(input("enter 3st no.:"))
Number(num1, num2, num3)

def Add():
    total = 0
    for i in range(1, 100):
        total += i
    print("the sum of all the nos.(1-100) is:",total)

Add()
"""
"""
print("10. Write a function that prints the multiplication table of a given number. ")
def Multiply(num):
    print("the multiplication of",num,"is:")
    for i in range(1, 11):
        print(num * i)

num = int(input("enter a no.:"))
Multiply(num)

print("11. Write a function to calculate and return the square of a number. ")
def Square(num):
    print("the square of",num,"is:",num * num)

num = int(input("enter a no.:"))
Square(num)

print("12. Write a function to calculate the factorial of a number using a loop. ")
def Factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of",num,"is:",fact)

num = int(input("enter a no.:"))
Factorial(num)

print("13. Write a function to check whether a number is prime. ")
def Prime(num):
    if num <= 1:
        print("Not a prime number")
        return
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            return
    print("Prime number")

num = int(input("Enter a number: "))
Prime(num)

print("14. Write a function to calculate the sum of digits of a number. ")
def SumDigits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    print("Sum of digits =", total)

num = int(input("Enter a number: "))
SumDigits(num)

print("15. Write a function that accepts a number n and returns the sum of all numbers from 1 to n.")
def Add(n):
    total = 0
    for i in range(0, n + 1):
        total += i
    print("the sum of all the nos.(1-n) is:",total)

n = int(input("Enter a number: "))
Add(n)

print("1. Create a list of 10 numbers and print all the elements.") 
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in numbers:
    print(i)

print("2. Write a program to find the largest element in a list.")
numbers = [10, 45, 23, 89, 12, 67, 34]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print("Largest element =", largest)

print("3. Write a program to find the smallest element in a list. ")
numbers = [10, 45, 23, 89, 12, 67, 34]
smallest = numbers[0]
for i in numbers:
    if i < smallest:
        smallest = i
print("Smallest element =", smallest)

print("4. Write a program to calculate the sum of all elements in a list. ")
numbers = [10, 20, 30, 40, 50]
total = 0
for i in numbers:
    total += i
print("Sum of all elements =", total)

print("5. Write a program to calculate the average of all elements in a list. ")
numbers = [10, 45, 23, 89, 12, 67, 34]
total = 0
for i in numbers:
    total += i
average = total / len(numbers)
print("Average =", average)

print("6. Write a program to count how many even numbers are present in a list. ")
numbers = [10, 15, 20, 25, 30, 35, 40]
count = 0
for i in numbers:
    if i % 2 == 0:
        count += 1
print("Number of even elements =", count)

print("7.	Write a program to create a new list containing only the odd numbers from an existing list.")
numbers = [10, 15, 20, 25, 30, 35, 40]
odd_numbers = []
for i in numbers:
    if i % 2 != 0:
        odd_numbers.append(i)

print("8. Write a program to find whether a given element exists in a list. ")
list = [10, 48, 57, 20, 36]
element = int(input("enter the element:"))
if element in list:
    print("element is in list")
else:
    print("element not in list")

print("9. Write a program to reverse a list without using any built-in reverse function.")
numbers = [10, 20, 30, 40, 50]
reversed_list = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])
print("Original List:", numbers)
print("Reversed List:", reversed_list)

print("10. Program to find the second largest element in a list.")
numbers = [10, 25, 45, 30, 50, 40]
largest = second_largest = numbers[0]
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("Second largest element =", second_largest)

print("1. Create a dictionary to store a student's name, age, and city, and print the dictionary. ")
student = {
    "name": "Samruddhi",
    "age": 18,
    "city": "Pune"
}
print(student)

print("2. Write a program to print all the keys of a dictionary.")
student = {
    "name": "Samruddhi",
    "age": 18,
    "city": "Pune"
}
for key in student:
    print(key)

print("3. Write a program to print all the values of a dictionary. ")
student = {
    "name": "Samruddhi",
    "age": 18,
    "city": "Pune"
}
for value in student.values():
    print(value)

print("4. Write a program to add a new key-value pair to an existing dictionary. ")
student = {
    "name": "Samruddhi",
    "age": 18,
    "city": "Pune"
}
student["grade"] = "A"
print(student)

print("5. Write a program to update the value of an existing key in a dictionary. ")
student = {
    "name": "Samruddhi",
    "age": 18,
    "city": "Pune"
}
print("before update:", student)
student["age"] = 19
print("after update:", student)

print("6. Write a program to check whether a given key exists in a dictionary. ")
student = {
    "name": "Samruddhi",
    "age": 18,
    "city": "Pune"
}
key = input("Enter a key to check: ")
if key in student:
    print("Key exists in dictionary")
else:
    print("Key does not exist in dictionary")

print("7. Write a program to remove a key-value pair from a dictionary. ")
student = {
    "name": "Samruddhi",
    "age": 18,
    "city": "Pune"
}
key = input("Enter a key to remove: ")
if key in student:
    del student[key]
    print("Key-value pair removed")
else:
    print("Key does not exist in dictionary")
print("Updated dictionary:", student)

print("8. Write a program to count the total number of key-value pairs in a dictionary. ")
student = {
    "name": "Samruddhi",
    "age": 18,
    "city": "Pune"
}
count = len(student)
print("Total number of key-value pairs:", count)

print("9. Write a program to iterate through a dictionary and print all keys and their corresponding values. ")
student = {
    "name": "Samruddhi",
    "age": 18,
    "city": "Pune"
}
for key, value in student.items():
    print(key, ":", value)

print("10. Create a dictionary of student names and marks, then find the student with the highest marks.")
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 96
}
highest_student = max(students, key=students.get)
print("Student with highest marks:", highest_student)