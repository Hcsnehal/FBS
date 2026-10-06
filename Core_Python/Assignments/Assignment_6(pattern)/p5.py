n = 5
for i in range(1, n + 1):
    if i == 1:
        print("        1")
    elif i == n:
        print("1   2   3   4   5")
    else:
        print("  " * (n - i), end="")
        print("1", end="")
        print(" " * (4 * i - 5), end="")
        print(i)