class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = []
        count ,res = 0 , 0
        while count < len(capacity):
            diff.append(capacity[count] - rocks[count])
            count += 1
        diff.sort()
        for i in diff:
            if additionalRocks - i >= 0:
                res += 1
                additionalRocks -= i
            else:
                break
        return res