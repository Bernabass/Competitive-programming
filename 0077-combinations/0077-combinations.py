class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def back_track(start, depth, pos_ans):
        
            if depth == k:
                ans.append(pos_ans.copy())
                return
               
    
            for curr in range(start, n+1):
                pos_ans.append(curr)
                back_track(curr+1, depth + 1, pos_ans)
                pos_ans.pop()
                
            return
        
        back_track(1, 0, [])
        
        return ans