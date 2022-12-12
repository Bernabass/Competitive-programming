class Solution:
    def climbStairs(self, n: int) -> int   : 
        root = 0
        stack = []
        best = {}
        while 1:
            if root  <= n:
                stack.append(root)
                root = root + 1
            else:
                p = stack.pop()
                if p + 1 > n:
                    best[p] = 1
                    while stack:
                        root = stack.pop()
                        temp = 0
                        if root + 1 <= n :
                            temp += best[root + 1]
                        if root + 2 <= n:
                            temp += best[root + 2]
                        best[root] = temp
                    return best[0]