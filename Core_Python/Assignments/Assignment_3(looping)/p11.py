# 11. WAP to check if given number Strong Number.

num = int(input("Enter number = "))

original = num
total = 0

while num > 0:
    digit = num % 10
    num = num // 10

    fact = 1
    i = 1

    while i <= digit:
        fact = fact * i
        i = i + 1

    total = total + fact

if total == original:
    print("Strong number")
else:
    print("Not a Strong number")
        