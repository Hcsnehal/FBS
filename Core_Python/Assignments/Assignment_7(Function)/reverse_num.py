# 8. Write a program find reverse of a number
def rev_num():
 num=int(input('enter a num:'))
 rev=0
 while(num>0):
    d=num%10 
    rev=rev*10+d 
    num=num//10 
 print('reveserve of num is :',rev)    
rev_num() 
   
