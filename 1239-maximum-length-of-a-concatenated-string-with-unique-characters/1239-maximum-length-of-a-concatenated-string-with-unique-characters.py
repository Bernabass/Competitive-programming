class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        max_len = [0]
        
        def is_valid(arr1, arr2):
            for char in arr1:
                if char in arr2:
                    return False
                
            return True
        

        def back_track(start, prev):
            if start == n:
                max_len[0] = max(max_len[0], len(prev))
                return
            
            curr = set(arr[start])
            if len(curr) == len(arr[start]) and is_valid(arr[start], prev):
                prev |= curr
                back_track(start+1, prev)
                prev -= curr
                
            back_track(start+1, prev)
            
            return
        
        back_track(0, set())
        
        return max_len[0]      