# Q4. Write a program to count the number of uppercase and lowercase letters in a string.
str='FirstBitSolution'
Upper=0
lower=0 
total=0
for i in str:
    if i >= 'A' and  i <='Z':
        Upper=Upper+1
    elif i >= 'a' and i<='z':
        lower=lower+1
    total=total+1    
print('uppercase letter in string=',Upper)    
print('lowercase letter in string =',lower)    
print('total',total)
         


