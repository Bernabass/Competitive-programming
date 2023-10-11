class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        count = 0
        MOD = 10**9 + 7

        for i in range(N):
            curr = target - nums[i]
            if curr < 0:
                break
            idx = bisect_right(nums, curr, i)

            size = idx - i
            if size:
                after = pow(2, size - 1, MOD) - 1
                count += (after + 1) % MOD
                
        return count % MOD