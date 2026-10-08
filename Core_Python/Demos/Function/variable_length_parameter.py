# def add(*data):
#     sum=0 
#     for val in data:
#         sum+=val 
#     return sum 
# res=add(1,23,45,65,4,4,3,9,0,6)
# print(res)     

def sum_num():
 num=int(input('enter a num='))
 sum=0
 i=1
 while(i<=num):
  sum=sum+i
  i+=1
 print(sum)  
sum_num()