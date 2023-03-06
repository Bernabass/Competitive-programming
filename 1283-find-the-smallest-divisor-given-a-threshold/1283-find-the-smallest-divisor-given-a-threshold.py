class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        test_cases = list(range(1, max(nums)+1))
        low = 0
        high = len(test_cases) - 1
        
        while low <= high:
            
            mid = (low+ high) // 2
            result = 0
            
            for i in nums:
                result += math.ceil( i / (test_cases[mid]))
                
            if low == high:
                return test_cases[mid]
            
            if result > threshold:
                low = mid + 1
                
            else:
                if mid-1 < 0:
                    return test_cases[mid]
                
                result = 0
                for i in nums:
                    result += math.ceil(i / (test_cases[mid-1]))
                    
                if result > threshold:
                    return test_cases[mid]
                
                high = mid-1