class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        prev, temp = Counter(words[0]), words.copy()
        res = []
        for i in range(1,n):
            curr = Counter(words[i])
            if curr == prev:
                temp[i] = 0
            prev = curr
            del curr
            
        for word in temp:
            if word:
                res.append(word)
                
        return res