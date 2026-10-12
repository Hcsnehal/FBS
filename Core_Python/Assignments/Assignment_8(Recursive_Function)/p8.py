# 8. Write a program to check whether a number is prime or not using recursion.

def prime(n, i):
    if i == n:
        return True
    elif n % i == 0:
        return False
    else:
        return prime(n, i + 1)
num = int(input("Enter number = "))
if num <= 1:
    print("Not Prime")
else:
    res = prime(num, 2)

    if res:
        print("Prime")
    else:
        print("Not Prime")