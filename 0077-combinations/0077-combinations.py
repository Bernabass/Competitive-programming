class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        start = 1
        end, depth = n + 1, k
        
        def merge(start, end, depth, ansX):
            if not depth:
                res.append(ansX)
                return

            for i in range(start, end):
                merge(i+1, end, depth-1, ansX + (i,))

        merge(start, end, depth, ())
        
        return res