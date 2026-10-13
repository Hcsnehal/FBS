# print all elements at odd index

li=[34,45,67,8,9,64,23]
for val in range(len(li)):
    if(val % 2 != 0):
        print(li[val])
    