# 12. Check if Two Strings Are Anagrams
# Input: "listen", "silent" → Output: True

str1 = "listen"
str2 = "silent"

if len(str1)==len(str2):
    print(' '.join(sorted(str1))==' '.join(sorted(str2)))

'''
or
str1 = "listen"
str2 = "silent"

# Check if sorted characters are equal
if sorted(str1) == sorted(str2):
    print(True)
else:
    print(False)


'''