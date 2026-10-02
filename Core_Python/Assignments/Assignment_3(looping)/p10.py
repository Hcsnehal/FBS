# 10. WAP to check if given number is Perfect Number.
num = int(input('enter a num='))
i=1
perfect_num=0
while(i<=num):
  if num%i==0 and i!=num:
    print(i)
    perfect_num=perfect_num+i   
  i+=1
if num == perfect_num:
      print('num is perfect..')
else:
      print('num is not perfect..')    