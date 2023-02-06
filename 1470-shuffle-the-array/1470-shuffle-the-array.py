class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ptr1, ptr2 = 0, n
        ans = []
        
        for i in range(n):
            ans.append(nums[i+ptr1]) 
            ans.append(nums[i+ptr2])
            
        return ans