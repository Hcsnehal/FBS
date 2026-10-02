#Find the sum of all even numbers from 1 to 50. 

i=1
sum=0
while(i<=50):
    if(i%2==0):
        sum=sum+i 
    i+=1
print(sum)          