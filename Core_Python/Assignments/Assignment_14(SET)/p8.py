# 8. Write a Python program to find all the anagrams and group them
# together from a given list of strings.

words = ['ram','sham','sita','gita','raj']
groups = {}
for word in words:
    key = ''.join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print("Anagram groups:", list(groups.values()))