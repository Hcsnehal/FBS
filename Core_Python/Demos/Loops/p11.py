#Take a number from the user and count how many digits it has using a while loop

num=int(input('enter a num='))   
i=0
count=0
while(num>0):
    di=num%10 
    count=count+1
    num=num//10
    i+=1
print(count)    

