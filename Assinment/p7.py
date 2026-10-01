
# 7. Write a program to solve the following series :

# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

# a. 1! + 2! + 3! + 4! + .....n!

num = int(input("Enter num = "))
i = 1
fact = 1
total = 0

while i <= num:
    fact = fact * i
    total = total + fact
    i = i + 1

print("Sum =", total)

# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent) 

num = int(input("Enter num = "))
i = 1
total = 0

while i <= num:
    total = total + num ** i
    i = i + 1

print("Sum =", total)


# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
num = int(input("Enter num = "))
i = 1
term = 1
total = 0

while i <= num:
    total = total + term
    term = term * 2
    i = i + 1
print("Sum =", total)


# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10 

a = int(input("Enter a = "))
i = 1
total = 0

while i <= 10:
    total = total + (a ** i) / i
    i = i + 1
print("S =", total)


# e. x - x2/3 + x3/5 - x4/7 + .... to n terms 

x = int(input("Enter x = "))
n = int(input("Enter n = "))

i = 1
den = 1
total = 0
while i <= n:
    term = (x ** i) / den

    if i % 2 == 0:
        total = total - term
    else:
        total = total + term

    den = den + 2
    i = i + 1
print("S =", total)