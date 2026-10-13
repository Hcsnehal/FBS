# 6. Print all even numbers using index.

# li=[2,5,7,51,8,10]
# for ind in range(0,len(li)):
#     if li[ind] % 2==0:
#       print(li[ind])


# 10. Count how many even numbers are present.
li = [2, 5, 7, 51, 8, 10]

count = 0

for ind in range(0, len(li)):
    if li[ind] % 2 == 0:
        count = count + 1

print(count)