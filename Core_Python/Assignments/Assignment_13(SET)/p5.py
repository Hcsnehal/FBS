# 5. Write a Python program to find the longest common prefix of all
# strings. Use the Python set.


words = ['snehal','gayatri','sita']
s = set(words)
prefix = ""

for i in range(min(len(word) for word in s)):
    chars = {word[i] for word in s}
    if len(chars) == 1:
        prefix += chars.pop()
    else:
        break
print("longest common pre=", prefix)