# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.

angle1 = int(input('enter first angle..'))
angle2 = int(input('enter second angle..'))
angle3 = int(input('enter third angle..'))

if(angle1 > 0 and angle2 > 0 and angle3 > 0 and angle1 + angle2 + angle3 == 180):
    print('triamgle is valid ')
else :
    print('angle is not valid ')    