class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        word1, word2 = deque(word1), deque(word2)
        res = []
        
        while word1 and word2:
            if word1 > word2:
                res.append(word1.popleft())
            else:
                res.append(word2.popleft())
        
        res.extend(word1)
        res.extend(word2)
        return "".join(res)