class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        def back_track(idx, prev, target, s):
            if idx == len(s):
                if prev == target:
                    return True
                
            for i in range(idx, len(s)):
                curr = int(s[idx:i+1])
           
                if curr + prev <= target:
                    if back_track(i+1, curr+prev, target, s):
                        return True
                    
                else:
                    return False
                    
        for i in range(1, n+1):
            pos_ans = i**2
            if back_track(0, 0, i, str(pos_ans)):
                ans += pos_ans
                
        return ans