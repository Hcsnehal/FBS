# 6. Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.

numbers = [2,3,4,5,6,7]
s = set(numbers)
max_product = 0
pair = ()
for a in s:
    for b in s:
        if a != b and a * b > max_product:
            max_product = a * b
            pair = (a, b)

print("Pair:", pair)
print("Maximum product:", max_product)