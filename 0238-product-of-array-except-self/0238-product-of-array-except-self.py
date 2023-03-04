class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [1]*n
        suffix_product = prefix_product = 1
        
        for i in range(n-1, -1, -1):
            arr[i] *= suffix_product
            suffix_product *= nums[i]
           
        for j in range(n):
            arr[j] *= prefix_product
            prefix_product *= nums[j]
            
        return arr