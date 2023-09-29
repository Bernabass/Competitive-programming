class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dictionary = set(wordDict)
        res = []
        N = len(s)
        
        def back_track(idx, constructed):
            if idx == N:
                res.append(" ".join(constructed))
                return
            
            
            for i in range(idx, N):
                curr = s[idx : i + 1]
                if curr in dictionary:
                    back_track(i + 1, constructed + [curr])
                    
                    
        back_track(0, [])
        
        return res               