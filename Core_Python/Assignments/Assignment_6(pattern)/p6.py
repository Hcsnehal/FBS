n = 5
for i in range(1, n + 1):
    if i == 1:
        for j in range(1, n + 1):
            print(j, end=" ")
        print()
    elif i == n:
        print(i)
    else:
        print(i, end="")
        print(" " * (2 * (n - i) - 1), end="")
        print(n)