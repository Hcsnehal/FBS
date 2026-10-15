# 9. Write a program to create three lists of numbers, their squares and cu

li = [11,23,34,56,14]

sq= []
cube = []

for val in li:
    sq.append(val ** 2)
    cube.append(val ** 3)

print("Numbers:", li)
print("Squares:", sq)
print("Cubes:", cube)
