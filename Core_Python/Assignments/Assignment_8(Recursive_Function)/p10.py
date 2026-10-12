# 10. Write a program to reverse a number using recursion.

def reverse(n, rev):
    if n == 0:
        return rev
    else:
        digit = n % 10
        rev = rev * 10 + digit
        return reverse(n // 10, rev)
num = int(input("Enter number = "))
res = reverse(num, 0)
print(res)