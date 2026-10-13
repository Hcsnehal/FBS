# 7. Write a program to create a new list from existing list which contains cube of
# each number of list.

li = [3,5,7,0,5]
new_li = []
for val in li:
    cube = val ** 3
    new_li.append(cube)
print(new_li)