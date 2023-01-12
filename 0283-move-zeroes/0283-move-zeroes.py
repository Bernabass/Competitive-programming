class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        priority = deque()
        
        for idx in range(len(nums)):
            if not nums[idx]:
                priority.append(idx)
            else:
                if priority:
                    new_idx = priority.popleft()
                    nums[new_idx] = nums[idx]
                    nums[idx] = 0
                    priority.append(idx)
