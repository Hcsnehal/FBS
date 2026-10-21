# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not

dic = {1: "ram", 2: "sham", 3: "sita"}

key = int(input("Enter the key= "))
if key in dic:
    print("Key exists")
else:
    print("Key does not exist")