class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num - 3) % 3 != 0:
            return []
        n = (num - 3) // 3
        return [n,n+1,n+2]