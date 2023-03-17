class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        mid = len(nums) // 2
        left_nums = self.sortArray(nums[:mid])
        right_nums = self.sortArray(nums[mid:])
        
        ptr_left = ptr_right = 0
        ans = []
        
        while ptr_left < len(left_nums) and ptr_right < len(right_nums):
            
            if left_nums[ptr_left] < right_nums[ptr_right]:
                ans.append(left_nums[ptr_left])
                ptr_left += 1
                
            else:
                ans.append(right_nums[ptr_right])
                ptr_right += 1
                
        ans.extend(left_nums[ptr_left:])
        ans.extend(right_nums[ptr_right:])
        
        return ans
        
        