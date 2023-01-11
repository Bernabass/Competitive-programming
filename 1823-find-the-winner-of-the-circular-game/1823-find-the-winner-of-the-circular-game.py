class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = 1
        for idx in range(2,n+1):
            res = (res + k - 1) % idx +1
            
        return res