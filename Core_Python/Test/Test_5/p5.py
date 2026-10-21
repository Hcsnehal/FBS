# 5. Python Program to Find the Union of two Lists without
# using set concept.

li1 = [9,7,6,5,4,2]
li2 = [8,4,3,2,1,5]
U = []
for i in li1:
    if i not in U:
        U.append(i)

for i in li2:
    if i not in U:
        U.append(i)
print(U)