# 3. Write a program to reverse a given number using recursive function.
def reverse(num, res):
    if num == 0:
        return res
    else:
        digit = num % 10
        res = res * 10 + digit
        return reverse(num // 10, res)

num = int(input("Enter number: "))
res = reverse(num, 0)
print(res)