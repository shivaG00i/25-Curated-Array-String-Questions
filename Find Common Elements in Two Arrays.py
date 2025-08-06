# 16. Find Common Elements in Two Arrays
# Input: [1,2,3], [2,3,4] → Output: [2,3]

list1 = [1, 2, 3]
list2 = [2, 3, 4]

# Convert both lists to sets and find intersection
common = set(list1).intersection(set(list2))

# Optionally convert back to list
print(list(common))  # Output: [2, 3]

'''
def common_elements(a: list[int], b: list[int]) -> list[int]:
    return list(set(a) & set(b))

OR 

def common_elements(a: list[int], b: list[int]) -> list[int]:
    return list(set(a).intersection(set(b)))


'''