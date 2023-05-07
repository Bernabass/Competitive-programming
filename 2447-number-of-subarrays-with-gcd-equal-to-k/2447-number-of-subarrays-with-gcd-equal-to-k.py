class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            curr_gcd = nums[i]
            ans += curr_gcd == k
            
            for j in range(i+1, len(nums)):
                curr_gcd = gcd(nums[j], curr_gcd)
                if nums[j] < k > curr_gcd :
                    break
                    
                ans += curr_gcd == k
                    
        return ans