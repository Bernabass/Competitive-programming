class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
              
        return max(max(left + [0]), n - min(right + [n]))
        
        """



        left = [3, 2]
        right = [1, 2]
        t = 1




        """