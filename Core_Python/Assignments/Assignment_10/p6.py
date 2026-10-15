# 6. Python Program to Find the Union of two Lists


li1 = [10, 20, 30, 40]
li2 = [30, 40, 50, 60]
union = []
for val in li1:
    if val not in union:
        union.append(val)
for val in li2:
    if val not in union:
        union.append(val)
print("Union of two lists:", union)
