class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2':"abc", '3':"def", '4':"ghi", "5":"jkl", "6":"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        
        ans = []
        def back_track(i, prev):
            if i == len(digits):
                if prev:
                    ans.append("".join(prev))
                return
            
            for char in mapping[digits[i]]:
                back_track(i + 1, prev + [char])
                
        back_track(0, [])
        
        return ans