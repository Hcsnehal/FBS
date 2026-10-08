def chkpalindrome(num):
    temp=num
    rev=0
    while(temp>0):
        d=temp%10
        temp=temp//10
        rev=rev*10+d 
    if(num==rev):
        return True 
    else:
        return False 
n=int(input('enter a num='))
print(chkpalindrome(n))        