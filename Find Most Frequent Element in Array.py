# 11. Find Most Frequent Element in Array
# Input: [3,1,3,2,3,4] → Output: 3

list1= [3,1,3,2,3,4]

# for i in list1:
#     if list1.count(i)>1:
#         print(list1.count(i))
#         break

freq={}
for num in list1:
    freq[num]=freq.get(num,0)+1

most_frq=max(freq,key=freq.get)
print(most_frq)