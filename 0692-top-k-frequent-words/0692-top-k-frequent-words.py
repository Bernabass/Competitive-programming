class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        freq = [-val for val in count.values()]
        pair = list(tuple(zip(freq, count.keys())))
        heapify(pair)        
        
        return [word for val, word in nsmallest(k, pair)]