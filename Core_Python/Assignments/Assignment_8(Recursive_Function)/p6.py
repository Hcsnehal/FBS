# 6. Write a program to print Fibonacci series using recursion.

def fibonacii(n):
    if n <= 2:
        return 1
    else:
        return fibonacii(n - 1) + fibonacii(n - 2)
num = int(input("Enter number of terms = "))
i = 1
while i <= num:
    print(fibonacii(i), end=" ")
    i = i + 1