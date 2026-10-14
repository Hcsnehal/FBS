# 15. Python Program to find larger string without using built-in functions.

str1 = "snehal"
str2 = "deshmukh"
count1 = 0
count2 = 0

for ch in str1:
    count1 = count1 + 1

for ch in str2:
    count2 = count2 + 1

if count1 > count2:
    print("Larger string:", str1)
elif count2 > count1:
    print("Larger string:", str2)
else:
    print("Both strings have equal length")