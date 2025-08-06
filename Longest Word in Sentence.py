# 14. Longest Word in Sentence
# Input: "we build software" → Output: "software"

Sentence =  "we build software"


max1=max(Sentence.split(),key=len)
print(max1)