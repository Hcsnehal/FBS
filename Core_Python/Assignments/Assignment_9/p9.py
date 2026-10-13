# 9. Write a program of having n number of elements in the list and find out even
# # and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

li = [2,4,5,7,8,9,22,11,32]
even_li = []
odd_li = []

for val in li:
    if val % 2 == 0:
        even_li.append(val)
    else:
        odd_li.append(val)

print("even list :", even_li)
print("odd list:", odd_li)