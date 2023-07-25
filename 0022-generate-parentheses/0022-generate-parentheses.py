class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def back_track(prev, opening, closing):
            if opening == closing == 0:
                ans.append("".join(prev))
                return
            
            if opening:
                back_track(prev + ["("], opening - 1, closing)
                     
            if closing and opening != closing:
                back_track(prev + [")"], opening, closing - 1)
                
                
        back_track([], n, n)
        
        return ans