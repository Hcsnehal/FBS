i = 1
while i <= 5:
    j = 1
    while j <= 5 - i:
        print(" ", end=" ")
        j = j + 1
    j = 1
    while j <= 2 * i - 1:
        print(chr(64 + j), end=" ")
        j = j + 1
    print()
    i = i + 1