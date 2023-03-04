class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1]
        suffix_product = deque([1])
        ans = []
        
        for i in range(n-1):
            prefix_product.append(prefix_product[-1]*nums[i])
            suffix_product.appendleft(suffix_product[0]*nums[n - 1 - i])
            
        for j in range(n):
            ans.append(prefix_product[j]*suffix_product[j])
            
        return ans