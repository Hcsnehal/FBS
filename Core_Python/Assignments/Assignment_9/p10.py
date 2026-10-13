# 10. Write a program to remove all occurrences of a given element in the list.

li = [10, 45,67,88,99,32,11]
tar = int(input("Enter element to remove: "))
new_li = []
for val in li:
    if val != tar:
        new_li.append(val)

print("Original list:", li)
print("Updated list:", new_li)