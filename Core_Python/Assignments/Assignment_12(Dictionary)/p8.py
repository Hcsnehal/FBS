# 8. Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary

s = input("enter s sting= ")
words = s.split()
dic = {}
for i in words:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)