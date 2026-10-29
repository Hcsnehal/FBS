# 7. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.

S1= {12,13,14,15,13,11}
S2 = {12,13,15,66,77,88}
missing_in_set2 = S1 - S2
missing_in_set1 = S2 - S1
print("Missing numbers in set2:", missing_in_set2)
print("Missing numbers in set1:", missing_in_set1)