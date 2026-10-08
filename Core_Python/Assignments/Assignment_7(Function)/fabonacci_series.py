# 6. Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms

def fibonacci(n):
    a = 1
    b = 1
    i = 1
    while i <= n:
        print(a)
        c = a + b
        a = b
        b = c
        i = i + 1
n = int(input("Enter n = "))
fibonacci(n)