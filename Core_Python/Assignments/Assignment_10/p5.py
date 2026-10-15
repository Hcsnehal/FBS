# 5. Python Program to Sort a List According to the Length of the Elements
# within the list.


li = ["ram", "sham", "RohitRaje", "duguubhaii", "ab"]
for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if len(li[i]) > len(li[j]):
            li[i], li[j] = li[j], li[i]
print(li)
