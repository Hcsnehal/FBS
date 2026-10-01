# 12. Write a program to check if given 3 digit number is a palindrome or not.

num= int(input('enter a num=')) #123

temp=num
d1 = num % 10 #3
snum = num//10 #12

d2 = snum%10 #2
snum2 = snum//10 #1

d3 = snum2 #1
rev = d1*100+d2*10+d3
print(rev)

if(temp==rev):
    print('number is palindrom..')
else:
    print('num is not palindrom..')    






