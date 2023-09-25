class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        primes = [n for n in range(1, max(nums) + 2) if is_prime(n)]
        N = len(primes)
        
        def calculate(curr, target):
            left, right = 0, len(primes) - 1
            while left < right:
                mid = (left + right) // 2

                if curr - primes[mid] > target:
                    if mid + 1 < N and curr - primes[mid + 1] > target:
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