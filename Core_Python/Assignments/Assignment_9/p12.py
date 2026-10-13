# 12. Write a program to create three lists of numbers, their squares
# and cubes

li = [3,4,5,6,7,8,9]
square_li = []
cube_li = []

for val in li:
    square_li.append(val ** 2)
    cube_li.append(val ** 3)
print("Numbers:", li)
print("Squares:", square_li)
print("Cubes:", cube_li)