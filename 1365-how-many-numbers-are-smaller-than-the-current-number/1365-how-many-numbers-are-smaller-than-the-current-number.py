class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        original = nums.copy()
        N = len(nums)
        left = right = 0
        nums.sort(reverse = True)
        smallers = defaultdict(int)
        ans = []
        
        while right < N:
            if nums[left] != nums[right]:
                smallers[nums[left]] += N - right
                left = right
            
            right += 1
        
        for num in original:
            ans.append(smallers[num])
            
        return ans