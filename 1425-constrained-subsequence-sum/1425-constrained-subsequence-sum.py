class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        queue = deque()
        N = len(nums)
        ans = 0
        for i in range(N):
            nums[i] += nums[queue[0]] if queue else 0
            ans = max(ans, nums[i])
            
            while queue and (i - queue[0] >= k or nums[i] >= nums[queue[-1]]):
                queue.pop() if nums[i] >= nums[queue[-1]] else queue.popleft()
                
            if nums[i] > 0:
                queue.append(i)
                
        return -1 if not ans else ans