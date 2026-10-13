def binaruySech(li,tar):
        start=0
        end=len(li)-1
        while start<=end:
            mid=(start+end)//2
            if tar==li[mid]:
                return mid
            elif tar<li[mid]:
                end=mid-1
            else:
                start=mid+1
        else:
            print("Element not found")
        return -1
li=[12,13,14,55,70,90]
tar=55
res=binaruySech(li,tar)
if res!=-1:
    print(f"Element is found at index {res}")        