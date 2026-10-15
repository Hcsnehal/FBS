# 8. Print 1 to 100 in snakes and ladder pattern.

num = 1

for i in range(10):
    li = []

    for j in range(10):
        li.append(num)
        num += 1

    if i % 2 == 1:
        li.reverse()

    print(*li, sep="\t")
