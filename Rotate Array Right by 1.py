# 13. Rotate Array Right by 1
# Input: [1,2,3,4] → Output: [4,1,2,3]

list1 = [1, 2, 3, 4]

v = list1.pop(-1)     # Remove last element (4)
list1.insert(0, v)    # Insert it at the beginning
print(list1)

''' 
list1 = [1, 2, 3, 4]
list1 = [list1[-1]] + list1[:-1]
print(list1)

'''