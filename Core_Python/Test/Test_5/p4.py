# 4. There is a list with some numbers. Create a new
# dictionary using this list in such a way that key is
# number and value is frequency of occurrence of that
# number in list.

li = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]
dic = {}
for i in li:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)