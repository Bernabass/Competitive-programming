class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        
        @cache
        def back_track(idx):       
            if idx == n:
                return True
            
            curr = ""
            for i in range(idx, n):
                curr += s[i]
                if curr in wordDict:
                    if back_track(i+1):
                        return True
                    
            return False
        
        return back_track(0)