class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        collections = set(words)
        ans = []
        
        @cache
        def dp(idx, s, length):
            if idx == len(s):
                return length > 1
            
            for i in range(idx, len(s)):
                if s[idx:i + 1] in collections:
                    if dp(i + 1, s, length + 1):
                        return True
                
        for word in words:
            if dp(0, word, 0):
                ans.append(word)
                
        return ans