class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        def is_prime(x):
            d = 2
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 1
                
            return x > 1 and True
        
        primes = [n for n in range(1, max(nums) + 2) if is_prime(n)]
        
        def calculate(curr, target):
            left, right = 0, len(primes) - 1
            while left < right:
                mid = (left + right) // 2

                if curr - primes[mid] > target:
                    if mid + 1 < len(primes) and curr - primes[mid + 1] > target:
                        left = mid + 1

                    else:
                        return primes[mid]

                else:
                    right = mid - 1

            return primes[left]
        
        prev = 0
        for i in range(len(nums)):
            org = nums[i]
            nums[i] -= calculate(nums[i], prev)
            if nums[i] <= prev:
                if org <= prev:
                    return False
                
                else:
                    nums[i] = org
            
            prev = nums[i]

        return True