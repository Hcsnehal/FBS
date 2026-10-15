# 2. Python Program to Merge Two Lists and Sort it

li1 = [1,2,3,4,5]
li2 = [6,7,8,9,10]
li3 = li1 + li2
for i in range(len(li3)):
    for j in range(i + 1, len(li3)):
        if li3[i] > li3[j]:
            li3[i], li3[j] = li3[j], li3[i]
print(li3)