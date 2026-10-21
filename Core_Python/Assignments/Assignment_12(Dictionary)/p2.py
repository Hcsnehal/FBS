# 2. Python Program to Concatenate Two Dictionaries Into One

# dic1= {1: "cat", 2: "dog"}
# dic2 = {3: "fish", 4: "snake"}

# dic1.update(dic2)
# print(dic1)


#without using built in
dic1= {1: "cat", 2: "dog"}
dic2 = {3: "fish", 4: "snake"}

for i in dic2:
    dic1[i] = dic2[i]
print(dic1)