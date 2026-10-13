def bubbleSort(li):
    for i in range(len(li)):
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    return li
    
li=[7,1,18,45,66,3]
print(f"Before Sorting List{li}")
l2=bubbleSort(li)
print(f"After sorting Sorting List{l2}")