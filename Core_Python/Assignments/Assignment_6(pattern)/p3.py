i = 1

while i <= 5:
    j = 1
    while j <= i:
        if i == 1 or i == 2 or i == 5:
            print(j, end=" ")
        elif j == 1 or j == i:
            print(j, end=" ")
        else:
            print(" ", end=" ")
        j = j + 1
    print()
    i = i + 1