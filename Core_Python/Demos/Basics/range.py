#range is built in function used to generate sequence of numbers 
# range(start,stop,step)

# Write a Python program to print all even numbers from 1 to 20 using range().
# for i in range(1,21):
#     if(i%2==0):
#         print(i) 

# for i in range(2,21,2):
#     print(i)

# Write a Python program using range() to print numbers from 10 to 1 in reverse order.
# for i in range(10,0,-1):
#     print(i)

# Print all multiples of 5 from 5 to 50 using range().

# for i in range(5,51):
#     if(i%5==0):
#         print(i)

# Print the squares of numbers from 1 to 10 using range().
# for i in range(1,11):
#    mul=i*i 
#    print(mul)   

# Print all numbers divisible by both 2 and 5 from 1 to 50.
# for i in range(1,51):
#     if(i%2==0 and i%5==0):
#         print(i)

# l1=[1,2,3,4,5]
# l2=[1,2,3,4,5]
# print(id(l1))
# l1.append(100)
# print(l1)
# print(id(l1))


# s = {10, 20, 30}
# print(id(s))
# s.add(700)
# print(id(s))
# print(s)

str='sinu'
# print(id(str))
str1='sinu'
print(id(str1))

str1=str+str1 
# print(str1)
print(id(str1))