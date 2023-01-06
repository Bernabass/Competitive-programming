class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counted = [0] * (max(costs)+ 1)
        res = 0
        for idx in costs:
            counted[idx] += 1
        counted = counted[1:]
        
        for val, freq in enumerate(counted,1):
            if val > coins:
                return res
            max_ = coins // val
            if max_ >= freq:
                res += freq
                coins -= val * freq
            else:
                res += max_
                coins -= max_ * val
        return res
            