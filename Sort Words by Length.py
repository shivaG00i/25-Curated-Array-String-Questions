# 17. Sort Words by Length
# Input: ["hi", "client", "is"] → Output: ["hi", "is", "client"]


list1=["hi", "client", "is"]

v=sorted(list1,key=len)
print(v)