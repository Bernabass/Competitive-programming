class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        info = [inf]*(amount+1)
        info[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if i-j >= 0:
                    info[i] = min(info[i], info[i-j]+1)
                            
        return -1 if info[amount] == inf else info[amount]