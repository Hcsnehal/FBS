# Python Program to count number of lowercase characters in a string.

str='WelCome'
count=0
for i in str:
    if i >='a' and i<='z':
        count+=1 
print(count)
