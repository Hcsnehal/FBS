# 10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions

str1='sinuydhsjkaknnwnweeeeeeeeeeeeeeeeeeeeeee'
str2='SnehalDeshmukh'
c_str1=0
c_str2=0

for i in str1:
    c_str1+=1
print('count of str1',c_str1)
for i in str2:
    c_str2+=1
print('count of str2',c_str2)    

if c_str1 > c_str2:
    print('string 1 is larger')
else:
    print('string 2 is larger ')    

