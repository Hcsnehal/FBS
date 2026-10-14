# Q5. Write a program to reverse a string without using slicing or string methods.
s = "Python"
rev = ""

for ch in s:
    rev = ch + rev

print(rev)