# 11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.

def count_digits(num):
    count = 0
    while num > 0:
        count = count + 1
        num = num // 10
    return count

def armstrong_sum(num, count):
    total = 0
    while num > 0:
        digit = num % 10
        total = total + digit ** count
        num = num // 10
    return total

def check_armstrong(num):
    count = count_digits(num)
    total = armstrong_sum(num, count)
    if total == num:
        return True
    else:
        return False

num = int(input("Enter number = "))
if check_armstrong(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")