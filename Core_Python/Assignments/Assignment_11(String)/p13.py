# 13. Python Program to count number of digits and letters in a string.

str='You are welcome 8189'
digits=0 
letters=0 
for i in str:
    if(i <= 'z' and i>='a'  or   i<='Z'  and i>='A'):
        letters=letters+1 
    if i >='0' and i<='9':
        digits=digits+1 
print('number of letters is =',letters)
print('number of digits is=',digits)        
