class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        stack = [0]
        next_greater = defaultdict(lambda:-1)
        
        for i in range(1, len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                next_greater[stack.pop()] = nums[i]
                
            stack.append(i)
         
        
        for idx in range(len(nums)//2):
            nums[idx] = next_greater[idx]
            
        return nums[:len(nums)//2]