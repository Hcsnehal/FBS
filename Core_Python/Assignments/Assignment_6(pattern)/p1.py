i = 1

while i <= 5:
    j = 1
    while j <= 5 - i:
        print(" ", end=" ")
        j = j + 1

    j = 1
    while j <= 2 * i - 1:
        if j == 1 or j == 2 * i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j = j + 1
    print()
    i = i + 1

i = 4
while i >= 1:
    j = 1
    while j <= 5 - i:
        print(" ", end=" ")
        j = j + 1

    j = 1
    while j <= 2 * i - 1:
        if j == 1 or j == 2 * i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        j = j + 1

    print()
    i = i - 1