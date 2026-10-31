# 2. Write a Python program to remove the intersection 
# of a second set with a first set.
S1={89,76,56,43,44,22}
S2 = {89,76,43,45,67}
S1.difference_update(S2)

print("Updated set1=", S1)