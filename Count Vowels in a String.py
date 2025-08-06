# 1. Count Vowels in a String
# Input: "architecture" → Output: 5

str1= 'architecture'


def count_vowels(s: str) -> int:
    count = 0
    vowel = 'aeiou'
    for char in s:
        if char.lower() in vowel:
            count += 1
    return count
print(count_vowels(str1))