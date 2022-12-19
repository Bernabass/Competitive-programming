class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def linear_ans(nums):
            money , n = 0 , len(nums)
            for i in range(n-1,-1,-1):
                temp =[0]
                if i + 2 < n:temp.append(nums[i+2])
                if i + 3 < n:temp.append(nums[i+3])
                nums[i] += max(temp)
                money = max(nums[i],money)
            return money
        nums1 = nums[1:]
        nums.pop()
        return max(linear_ans(nums1),linear_ans(nums))