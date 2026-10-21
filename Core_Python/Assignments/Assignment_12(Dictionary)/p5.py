# 5. Python Program to Sum All the Items in a Dictionary
dic = {1: 5, 2: 9, 3: 30, 4: 80}
total = 0
for i in dic:
    total = total + dic[i]
print("sum of all elements =", total)