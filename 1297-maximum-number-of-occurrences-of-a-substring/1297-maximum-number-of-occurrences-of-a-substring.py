class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        uniques = defaultdict(int)
        left = max_occurence = 0
        freq = defaultdict(int)
        
        
        for right in range(len(s)):
            uniques[s[right]] += 1
            
            while right - left + 1 > minSize:
                
                uniques[s[left]] -= 1
                if not uniques[s[left]]:
                    del uniques[s[left]]
                    
                left += 1
                
            if len(uniques) <= maxLetters and right - left + 1 == minSize:
                freq[s[left:right+1]] += 1
            
            
    
        if not freq:
            return 0
        
        return max(freq.values())  