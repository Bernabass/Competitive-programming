class Solution:
    def rob(self, nums: List[int]) -> int:
        money , n = 0 , len(nums)
        for i in range(n-1,-1,-1):
            temp =[0]
            if i + 2 < n:temp.append(nums[i+2])
            if i + 3 < n:temp.append(nums[i+3])
            nums[i] += max(temp)
            money = max(nums[i],money)
        return money