class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            currGcd = nums[i]
            if currGcd == k:
                ans += 1
            for j in range(i+1, len(nums)):
                if nums[j] < k:
                    break
                currGcd = gcd(nums[j], currGcd)
                if currGcd == k:
                    ans += 1
                    
                elif currGcd < k:
                    break
                    
        return ans