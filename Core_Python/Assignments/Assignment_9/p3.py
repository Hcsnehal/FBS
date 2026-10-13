# 3. Write a program to find the second largest element in the list.

li=[10,20,30,40,50,60,70,80,90]
max=li[0]
Second_largest=li[0]

for i in range(0,len(li)):
    if li[i] > max:
        Second_largest=max
        max=li[i]
 
    elif li[i] > Second_largest and li[i] != max:
        Second_largest=li[i]
print('second largest element is =',Second_largest)