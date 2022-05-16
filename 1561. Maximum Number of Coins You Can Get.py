class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        limit=(len(piles)/3)
        counter=1
        output=0
        for i in range(1,len(piles),2):
            if counter<=limit:
                output+=piles[i]
                counter+=1
            else:
                break
        return output