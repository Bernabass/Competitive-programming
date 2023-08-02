class Solution:
    def countAndSay(self, n: int) -> str:
        
        def say(string):
            string.append("a")
            res = []
            count, prev = 1, string[0]
            
            for i in range(1, len(string)):
                if string[i] != prev:
                    res.append(str(count))
                    res.append(prev)
                    prev = string[i]
                    count = 1
                    
                else:
                    count += 1
                    
            return res
        
        def dp(n):
            if n == 1:
                return ["1"]
            
            return say(dp(n - 1))
            
        return "".join(dp(n))