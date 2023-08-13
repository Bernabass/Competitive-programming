class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        
        def find(target):
            i = count = 0
            j = len(nums) - 1
            
            while i <= j:
                if nums[i] + nums[j] <= target:
                    count += j - i
                    i += 1
                    
                else:
                    j -= 1
                    
            return count
                     
        return find(upper) - find(lower - 1)