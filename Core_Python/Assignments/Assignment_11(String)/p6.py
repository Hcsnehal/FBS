# 6. Python Program to Take in a String and Replace Every Blank Space
# with Hyphen

# str='snehal deshmukh'
# new_str=str.replace(' ','_')
# print(new_str)

str='snehal deshmukh'
new_str=''
for i in str:
    if i == ' ':
        new_str=new_str+'_'
    else:
        new_str=new_str+i
print(new_str)         