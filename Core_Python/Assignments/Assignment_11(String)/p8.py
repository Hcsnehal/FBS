# 8. Python Program to Remove the Characters of Odd Index Values in a
# String

str='welcometohome'
new_str=''
for i in range(len(str)):
    if i % 2==0:
        new_str=new_str+str[i]
print(new_str)       
        
