class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        left = right = Ws = 0
        for _ in range(k):
            if blocks[right] == "W":
                Ws += 1
            right += 1
        ans = Ws
    
        while right < n:
            if blocks[left] =="W":
                Ws -= 1
            if blocks[right] == "W":
                Ws += 1
    
            ans = min(ans,Ws)
            left += 1
            right += 1
        return ans