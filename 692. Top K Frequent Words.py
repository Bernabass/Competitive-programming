class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        temp=Counter(words)
        out=[]
        final=[]
        print(temp)
        for i in temp:
            temp[i]=-temp[i]
            out.append([temp[i],i])
        heapq.heapify(out)
        print(out)
        for j in range(k):
            final.append(heapq.heappop(out)[1])
        return final