# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).

n = int(input("enter n="))
dic = {}
for i in range(1, n + 1):
    dic[i] = i * i
print(dic)