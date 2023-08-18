class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        GCD = numsDivide[0]
        deletion = 0
        for i in range(1, len(numsDivide)):
            GCD = gcd(GCD, numsDivide[i])
        
        freq = Counter(nums)
        nums = sorted(set(nums))
        for num in nums:
            if gcd(GCD, num) == num:
                return deletion
            
            deletion += freq[num]
            
        return -1