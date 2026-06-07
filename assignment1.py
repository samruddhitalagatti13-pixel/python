print("1. Positive or Negative")
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

print("2. Even or Odd")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

print("3. Greater of Two Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Greater number is", a)
else:
    print("Greater number is", b)

print("4. Voting Eligibility")
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

print("5. Divisible by 5")
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

print("6. Leap Year")
year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

print("7. Vowel or Consonant")
ch = input("Enter a character: ")
if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")

print("8. Largest Among Three Numbers")
a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    print(a)
elif b >= c and b >= a:
    print(b)
else:
    print(c)

print("9. Grade Assignment")
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

print("10. Number Between 1 and 100")
num = int(input("Enter a number: "))
if 1 <= num <= 100:
    print("Within range")
else:
    print("Out of range")

print("11. Print Numbers from 1 to 10 using for Loop")
for i in range(1, 11):
    print(i)

print("12. Print Numbers from 10 to 1 using for Loop")
for i in range(10, 0, -1):
    print(i)

print("13. Print Even Numbers from 1 to 20 using for Loop")
for i in range(2, 21, 2):
    print(i)

print("14. Print Odd Numbers from 1 to 20 using for Loop")
for i in range(1, 21, 2):
    print(i)

print("15. Sum of Numbers from 1 to 100 using for Loop")
total = 0
for i in range(1, 101):
    total += i
    print(total)

print("16. Multiplication Table using for Loop")
num = int(input("Enter number: "))
for i in range(1, 11):
    print(num * i)

print("17. Pattern using Nested for Loop")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
        print()

print("18. Print Each Character of a String")
text = input("Enter a string: ")
for ch in text:
    print(ch)

print("19. Factorial using for Loop")
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
    print("Factorial =", fact)

print("20. Reverse Star Pattern")
for i in range(5, 0, -1):
    print("*" * i)

print("21. Print Numbers from 1 to 10 using while Loop")
i = 1
while i <= 10:
    print(i)
    i += 1

print("22. Print Numbers from 10 to 1 using while Loop")
i = 10
while i >= 1:
    print(i)
    i -= 1

print("23. Print Even Numbers from 1 to 20 using while Loop")
i = 2
while i <= 20:
    print(i)
    i += 2

print("24. Print Odd Numbers from 1 to 20 using while Loop")
i = 1
while i <= 20:
    print(i)
    i += 2

print("25. Sum of Numbers from 1 to 100 using while Loop")
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
    print(total)

print("26. Multiplication Table using while Loop")
num = int(input("Enter number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

print("27. Count Number of Digits")
num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
    print("Digits =", count)

print("28. Reverse a Number")
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
    print("Reverse =", rev)

print("29. Factorial using while Loop")
n = int(input("Enter number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
    print("Factorial =", fact)

print("30. Password Validation")
password = "python123"
while True:
    user = input("Enter password: ")
    if user == password:
        print("Access Granted") 
        break
    else:
        print("Wrong Password")

