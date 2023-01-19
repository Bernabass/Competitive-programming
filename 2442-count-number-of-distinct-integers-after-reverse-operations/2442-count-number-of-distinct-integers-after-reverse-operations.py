class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        ptr = 0
        nums = list(map(str,nums))
        
        while ptr < n:
            curr = nums[ptr]
            nums.append(curr[::-1].lstrip("0"))
            ptr += 1
        
        return len(set(nums))