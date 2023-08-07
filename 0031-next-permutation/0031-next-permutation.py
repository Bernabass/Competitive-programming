class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        def do(idx):
            flag = True
            while flag:
                flag = False
                for k in range(idx + 1, n):
                    if nums[k] < nums[k - 1]:
                        nums[k], nums[k - 1] = nums[k - 1], nums[k]
                        flag = True
        
        for i in range(n - 1, -1, -1):
            curr = inf
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    if curr == inf or nums[j] < nums[curr]:
                        curr = j
                    
            if curr != inf and nums[curr] != nums[i]:
                nums[i], nums[curr] = nums[curr], nums[i]
                do(i + 1)
                return
            
        nums.sort()