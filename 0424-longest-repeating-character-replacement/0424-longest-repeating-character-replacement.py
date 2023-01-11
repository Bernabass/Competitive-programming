class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = max_size = 0
        prev = defaultdict(int)
        
        for right in range(n):
            prev[s[right]] += 1
            
            if (right - left + 1 - max(prev.values())) > k:
                prev[s[left]] -= 1
                left += 1
            max_size = max(max_size, right - left + 1)
            
        return max_size