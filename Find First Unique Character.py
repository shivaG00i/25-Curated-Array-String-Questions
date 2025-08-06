# 9. Find First Unique Character
# Input: "success" → Output: "u"

str1 = "success"

for cha in str1:
    if str1.count(cha) == 1:
        print(cha)
        break
