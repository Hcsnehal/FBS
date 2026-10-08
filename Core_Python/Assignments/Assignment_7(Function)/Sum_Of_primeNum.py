# 5. Sum of all prime numbers between 1 to n
def prime_sum(n):
    total = 0
    num = 2
    while num <= n:
        i = 2
        check = 0
        while i < num:
            if num % i == 0:
                check = 1
                break
            i = i + 1
        if check == 0:
            total = total + num
        num = num + 1
    return total
n = int(input("Enter n = "))
print("Sum =", prime_sum(n))