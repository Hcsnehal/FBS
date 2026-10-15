# 7. Python Program to Find the Intersection of Two Lists

li1 = [1,2,3,4,5]
li2 = [4,5,6,7,8]
interracttion_li1li2 = []
for val in li1:
    if val in li2 and val not in interracttion_li1li2:
        interracttion_li1li2.append(val)
print("Intersection of two lists:", interracttion_li1li2)
