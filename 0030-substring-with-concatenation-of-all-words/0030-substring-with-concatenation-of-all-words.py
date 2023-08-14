class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n1, n2 = len(s), len(words)
        n3 = len(words[0])
        x = n3 * n2
        words = Counter(words)
        ans = []
        
        @cache
        def IsValid(i, j):
            used = defaultdict(int)
            idx = i
            
            while idx <= j:
                curr = s[idx:idx + n3]
                
                if curr in words and words[curr] - used[curr] > 0:
                    used[curr] += 1
                    idx += n3
                
                else:
                    return False
            
            return True
        
        idx = 0
        while idx <= n1 - x + 1:
            if IsValid(idx, idx + x - 1):
                ans.append(idx)

            idx += 1
                
        return ans