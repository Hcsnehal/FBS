
n = 10

for i in range(n):
    if i == 0:
        print("*" * (2 * n + 1))
    elif i == n - 1:
        print("*" * (2 * n) + " *")
    else:
        print(" " * (2 * n - i) + "*")
