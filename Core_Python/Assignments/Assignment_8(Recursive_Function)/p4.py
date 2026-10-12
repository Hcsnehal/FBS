# 4. Write a program to find sum of n numbers using recursion.

def sumNum(n):
    if n <= 0:
        return 0
    else:
        return n + sumNum(n - 1)
num = int(input("Enter number: "))
res = sumNum(num)
print(res)