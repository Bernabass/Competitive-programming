class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        a = {}

        for word in words:
            if word in a:
                a[word] += 1
            else:
                a[word] = 1

        l = list(a.items())
        l = [(-j,i) for i,j in l]
        heapq.heapify(l)
        ret = []
        for i in range(k):
            _,w = heapq.heappop(l)
            ret.append(w)
        return ret