#5. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.


li = [89,34,56,77,33,22,13,22,22]
num = int(input("Enter a number = "))
count = 0
for val in li:
    if val == num:
        count = count + 1
if count > 0:
    print("Element is present in the list")
    print("Number of times present =", count)
else:
    print("Element is not present in the list")

