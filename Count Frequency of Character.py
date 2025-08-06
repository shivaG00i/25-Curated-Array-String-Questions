# 7. Count Frequency of Character
# Input: ("success", "s") → Output: 3

from collections import Counter


str1= "success"
count1= 's'

count = Counter(str1)
print(count[count1])

'''
or 

def count_char(s: str, target: str) -> int:
    count = 0
    for char in s:
        if char == target:
            count += 1
    return count


'''