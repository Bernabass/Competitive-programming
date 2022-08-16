from collections import Counter
import heapq
nums = [4,1,-1,2,-1,2,3]
k = 2
out=[]
count=Counter(nums)
lis=list(zip(count.values(),count.keys()))
heapq._heapify_max(lis)
klargest=heapq.nlargest(k,lis)
print(klargest)
for i in range(k) :
    out.append(klargest[i][1])
print(out)