class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans, stack = [-1]*n, [0]
        
        for idx in range(n*2):
            i = idx % n
            while stack and nums[i] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i]
                
            stack.append(i)
         
        return ans