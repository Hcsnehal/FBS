# 8. Write a program to create a duplicate of an existing list. It should not point to
# same list.


li = [1,4,5,90,87,22]
new_li = []
for val in li:
    new_li.append(val)
print("Original list:", li)
print("Duplicate list:", new_li)
# print(id(li))
# print(id(new_li))
