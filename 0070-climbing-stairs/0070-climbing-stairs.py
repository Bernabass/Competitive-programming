class Solution:
    def climbStairs(self, n: int) -> int   : 
        stack, best = -1 , {}
        while 1:
            if stack + 1  <= n:stack += 1
            else:
                best[stack] = 1
                while stack >= 0:
                    stack -= 1
                    temp = 0
                    if stack + 1 <= n :temp += best[stack + 1]
                    if stack + 2 <= n:temp += best[stack + 2]
                    best[stack] = temp
                return best[0]