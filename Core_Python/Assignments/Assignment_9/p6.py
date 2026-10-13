#6. Write a program to remove duplicates from the list.
     
li = [67,89,67,23,45,23,23,89,10,20]
new_li = []
for val in li:
    if val not in new_li:
        new_li.append(val)
print(new_li)