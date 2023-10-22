class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        queue = deque()
        ans = []

        for right in range(N):
            
            while queue and queue[0] < right - k + 1:
                queue.popleft()

            while queue and nums[right] >= nums[queue[-1]]:
                queue.pop()

            queue.append(right)

            if right >= k - 1:
                ans.append(nums[queue[0]])

        return ans