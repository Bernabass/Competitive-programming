class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def ispossible(min_weight):
            d=days
            count=0
            for i in weights:
                if i+count>min_weight:
                    d-=1
                    count=0
                count+=i
                if d==0:
                    return False
            return True
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+ high)//2
            if ispossible(mid):
                high=mid
            else:
                low = mid+1
        return low