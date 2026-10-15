# 4. Python Program to Find the Second Largest Number in a List Using Bubble
# Sort


li = [67,89,90,43,45,65,12]
n = len(li)

for i in range(n):
    for j in range(0, n - i - 1):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]

print("Sorted list:", li)
print("Second largest number:", li[-2])
