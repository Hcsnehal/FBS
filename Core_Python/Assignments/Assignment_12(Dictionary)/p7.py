# 7. Python Program to Remove the Given Key from a Dictionary
dic= {1: "ram", 2: "sita", 3: "gita", 4: "raj"}
key = int(input("enter key to remove="))
if key in dic:
    del dic[key]
    print('key exist',dic)
else:
    print('key does not exists')