class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        seen = {}
        for word in sorted(words, key=len): 
            seen[word] = 1
            for i in range(len(word)): 
                key = word[:i] + word[i+1:]
                if key in seen: 
                    seen[word] = max(seen[word], 1 + seen[key])
                    
        return max(seen.values())