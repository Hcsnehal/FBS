#Take a number from the user and find the sum of its digits using a while loop. 

num=int(input('enter a num='))   #235
sum=0
i=1
while(num>0):
    di=num%10 #5
    num=num//10  #23
    sum=sum+di  
    i+=1
print(sum)    
    

