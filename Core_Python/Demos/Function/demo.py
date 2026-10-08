# def addition(a,b):
#     c=a+b 
#     print(f'value of c is ={c}')
# addition(2,3)    

# def addition():
#     a=10
#     b=20
#     c=a+b 
    
#     return c
# res=addition()    
# print(f'addition is {res}')

# def addition(a,b):
#     c=a+b 
#     return c
# res=addition(2,3) 
# print(res)  


# 1.Default parameter

# def emp(id,name,sal,dept=''):
#     print('ID:',id)
#     print('salary :',sal)
#     print('name :',name)
#     print('department:',dept)
# emp(101,'snehal',50000)    

# 2.keyword parameter

# def emp(id,name,sal,dept):
#     print('ID:',id)
#     print('salary :',sal)
#     print('name :',name)
#     print('department:',dept)
# emp(101,dept='mba',name='snehal',sal=900000)  

# 3.variable length parameter concept 

# def emp(*data):
#     sum=0
#     for val in data:
#         sum+=val 
#     return sum 
# res=emp(1,2,3,4,5)  
# print(res)  

# 4.keyword variable length concept 
# def emp(**data):
#     for key,val in data.items():
#         print(key,':',val)
# emp(id=101,name='snehal')        

# recursion

   