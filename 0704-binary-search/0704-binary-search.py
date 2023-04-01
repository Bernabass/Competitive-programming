class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def index(a, x):
            i = bisect_left(a, x)
            if i != len(a) and a[i] == x:
                return i
            
            return -1
        
        return index(nums, target)