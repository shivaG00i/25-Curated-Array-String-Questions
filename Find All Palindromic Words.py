# 15. Find All Palindromic Words
# Input: ["wow", "radar", "client"] → Output: ["wow", "radar"]


list1 = ["wow", "radar", "client"]
list2=[]
for char in list1:
    if char==char[::-1]:
        list2.append(char)
print(list2)