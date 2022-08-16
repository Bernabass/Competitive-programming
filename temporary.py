from collections import Counter
import heapq
nums = [3,2,1,5,6,4]
k = 2
for i in range(len(nums)):
    nums[i]=-nums[i]
heapq.heapify(nums)
for j in range(k):
    out=heapq.heappop(nums)
print(-out)