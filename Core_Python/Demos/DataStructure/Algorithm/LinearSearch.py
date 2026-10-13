def LinearSearch(li,tar):
    for a in range(len(li)):
        if li[a]==tar:
            return a 
    else:
        return -1 
li=[23,45,66,78,90,12,23]
res=LinearSearch(li,100)
if res==-1:
    print('element not found..')
else:
    print(f'element is found at index {res}')          
