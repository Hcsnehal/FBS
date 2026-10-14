# 14. Python Program to count the occurrences of each word in a string.
str1 = "welcome home dear"
words = str1.split()
count = {}
for word in words:
    if word in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1

print(count)