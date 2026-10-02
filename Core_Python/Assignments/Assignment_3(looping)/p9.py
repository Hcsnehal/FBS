# 9. WAP to print all numbers in a range divisible by a given number.

num = int(input('enter a num='))
given_num = int(input('enter a another num='))
i=1
while(i<=num):
    if(i%given_num==0):
        print(i)
    i+=1    
    