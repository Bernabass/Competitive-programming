class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        minOpr = Ws = blocks[:k].count("W")
        for idx in range(k,n):
            if blocks[idx] == "W":
                Ws += 1
            if blocks[idx-k] == "W":
                Ws -= 1
            minOpr = min(minOpr,Ws)
            
        return minOpr