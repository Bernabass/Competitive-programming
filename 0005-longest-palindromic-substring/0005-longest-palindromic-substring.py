class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_sub = s[0]
                    
        def build(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1

                right += 1

            return s[left + 1:right]
        
        for idx in range(n):
            pal_1 = build(idx, idx)
            pal_2 = build(idx, idx + 1)
            
            if len(pal_1) > len(pal_2):
                curr_max = pal_1
                
            else:
                curr_max = pal_2
            
            if len(curr_max) > len(max_sub):
                max_sub = curr_max

        return max_sub