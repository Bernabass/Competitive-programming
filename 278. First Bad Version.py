# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low=1
        high=n
        mid=1
        while low<=high:
            mid=(low+high)//2
            if high==mid:
                return mid
            elif isBadVersion(mid):
                high=mid
            else:
                low=mid+1
        return mid      