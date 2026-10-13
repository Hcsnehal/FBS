# li=[1,2,3,4,5,12]
# li2=[1,2,3,4,5,89]
# print(id(li))
# print(id(li2))

# li=[1,2,3,4]
# for i in range(1,len(li)+1):
#     if(i%2==0):
#         print(i)
    
# 2. Access elements
# Create a list of 5 numbers and print:
# the first element
# the last element

# li=[12,34,45,43,28]
# print(li[0] and li[4])
# print(li[0] or li[4])

# li=[12,34,45,43,28]
# li[1]=100
# print(li)

 

# 6. Create a list of 5 numbers and print each element using a for loop.

# 7. Create a list of numbers and find the sum of all elements.

# 8. Create a list of numbers and find the largest number in the list.

# 9. Create a list of numbers and count how many even numbers are present.

# 10. Create a list of numbers and check whether a given number is present in the list or not.

# li=[23,34,45,56,67]
# for val in li:
#     print(val)

# li=[2,3,4,5,6,1]
# sum=0
# for val in li:
#     sum=sum+val 
# print(sum)   
# # 
# li=[23,34,44,90,10]
# max=li[1]
# for val in li:
#     if(val > max):
#        max=val 
# print(max)       

# 9. Create a list of numbers and count how many even numbers are present.
# li=[2,4,6,1,7,19,10,20,23]
# count=0
# for val in li:
#     if(val % 2==0):
#         count=count+1
# print(count)        

# 10. Create a list of numbers and check whether a given number is present in the list or not.                   

# num=int(input('enter a num='))
# li=[23,12,2,67,89,90]

# for val in li:
#     if(num==val):
#         print("found")
    



# li = [1, 2, 3, 4, 5]
# rev=[]
# for i in range(len(li)-1,-1,-1):
#     rev.append(li[i])
# print(rev)    

# li=[1,2,3,3,4,4,5]
# new_li=[]
# for val in li:
#     if val not in new_li:
#         new_li.append(val)
# print(new_li)     
# 
#    
# Write a program to create a new list from existing list which contains cube of
# each number of list.

# li=[2,3,4,5,6]
# new_li=[]
# for val in li:
#     cube=val*val*val 
#     new_li.append(cube)
# print(new_li)    
    
# 8. Write a program to create a duplicate of an existing list. It should not point to
# same list.

# li=[1,2,3,4,5]
# new_li=[]
# for val in li:
#     new_li.append(val)
# print(new_li)    



