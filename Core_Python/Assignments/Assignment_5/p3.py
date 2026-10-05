n = 4
i = 0
while i < n:
    j = 0
    while j <= i:
        if j == 0 or j == i:
            print(1, end=" ")
        else:
            print(i, end=" ")
        j = j + 1
    print()
    i = i + 1