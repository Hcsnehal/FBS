# 6. Write a program to print first n prime numbers.

n = int(input("Enter n = "))
num = 2
count = 0

while count < n:
    i = 2
    check = 0
    while i < num:
        if num % i == 0:
            check = 1
            break
        i = i + 1

    if check == 0:
        print(num)
        count = count + 1
    num = num + 1