# 5. Write a program to print prime numbers between 1 to 100.

num = 2
while num <= 100:
    i = 2
    count = 0

    while i < num:
        if num % i == 0:
            count = count + 1
        i = i + 1

    if count == 0:
        print(num)
    num = num + 1