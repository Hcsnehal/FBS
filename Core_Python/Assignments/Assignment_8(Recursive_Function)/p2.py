# 2. Write a program to check if given number is Armstrong or not using recursive
# function.

def armstrong(num, count):
    if num == 0:
        return 0
    else:
        digit = num % 10
        return digit ** count + armstrong(num // 10, count)
num = int(input("Enter number: "))
count = len(str(num))
res = armstrong(num, count)

if res == num:
    print("Armstrong number")
else:
    print("Not Armstrong number")