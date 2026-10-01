# 4. Write a program to input all sides of a triangle and check whether triangle is valid or not.

side1 = int(input('enter first side of triangle..'))
side2 = int(input('enter second side of triangle..'))
side3 = int(input('enter third side of triangle..'))

if (side1+side2 > side3 and side2+side3 > side1 and side1+side3 > side2):
    print('triangle is valid..')
else:
    print('triangle is not valid..')    