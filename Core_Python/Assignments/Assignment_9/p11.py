# 11. Write a program to print all numbers which are divisible by m and n in the
# list.
li = [5,6,7,8,9,3,2,8]
m = int(input("Enter m = "))
n = int(input("Enter n = "))

for val in li:
    if val % m == 0 and val % n == 0:
        print(val)