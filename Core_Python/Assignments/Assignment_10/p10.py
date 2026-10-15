# 10. Write a program to print list after removing even numbers.


li = [34,40,50,12,23,10,90]
new_li = []

for val in li:
    if val % 2 != 0:
        new_li.append(val)
print("Original list:", li)
print("List after removing even numbers:", new_li)
