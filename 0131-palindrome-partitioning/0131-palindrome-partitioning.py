class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        ans = []
        
        def Is_palindrome(arr):
            return arr == arr[::-1]
        
        def back_track(idx, prev):
            if idx == N:
                ans.append(prev.copy())
                return
            
            for i in range(idx, N):
                curr = s[idx : i + 1]
                if Is_palindrome(curr):
                    back_track(i + 1, prev + [curr])
                    
        back_track(0, [])   
                    
        return ans
                    