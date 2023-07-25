class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = s[0]
        n = len(s)
        
        def check(idx):
            curr_len1 = curr_len2 = s[idx]       

            i, j = idx - 1, idx + 1
            k, l = idx - 1, idx + 2
            
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    curr_len1 = s[i] + curr_len1 + s[j]
                    i -= 1
                    j += 1

                    
                else:
                    break
             
            if len(set(s[idx:idx+2])) == 1:
                curr_len2 = s[idx:idx+2]
                while k >= 0 and l < len(s):
                    if s[k] == s[l]:
                        curr_len2 = s[k] + curr_len2 + s[l]
                        k -= 1
                        l += 1

                    else:
                        break
                    
            if len(curr_len1) > len(curr_len2):
                return curr_len1
              
            return curr_len2
            
        for idx in range(n):
            curr = check(idx)
            if len(curr) > len(max_len):
                max_len = curr
            
        return max_len