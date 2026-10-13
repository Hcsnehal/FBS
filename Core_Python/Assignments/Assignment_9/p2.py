# 2. Write a program to find maximum and minimum element in a list.
li=[10,20,30,40,50,60,70,80,90]
max=li[0]
min=li[0]
for i in range(0,len(li)):
    if li[i] > max:
        max=li[i]
    
    if li[i] < min:
        min=li[i]    
print('maximum element is=',max)    
print('minimum element is=',min)        