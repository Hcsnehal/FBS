# 4. Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.

numbers = [1,2,3,4,5,6,7,8,9,0]
target = 3

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])