n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(f"{j:<2}", end="")
    print(" " * (4 * (n - i) + 1), end="")
    for j in range(i, 0, -1):
        print(f"{j:<2}", end="")

    print()