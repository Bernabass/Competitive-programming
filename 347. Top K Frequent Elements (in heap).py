class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out=[]
        count=Counter(nums)
        lis=list(zip(count.values(),count.keys()))
        heapq._heapify_max(lis)
        klargest=heapq.nlargest(k,lis)
        for i in range(k) :
            out.append(klargest[i][1])
        return out       