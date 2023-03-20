class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        total = sum(nums)
        memo = defaultdict(list)
        
        def pick(start, end):
            bound = [start, end]
            if (start, end) in memo:
                return memo[(start, end)]
            
            if start == end:
                return 0, 0
            
            if end - start == 1:
                return nums[start], nums[start]
            
            
            left = nums[start]
            start += 1

            if start == pick(start, end)[0]: start += 1
                
            else: end -= 1
            
            picked = pick(start, end)
            left_sum = left + picked[1]
             
            start, end = bound
            right = nums[end - 1]
            end -= 1
                        
            if start == pick(start, end)[0]: start += 1
            
            else: end -= 1
            
            picked = pick(start, end)
            right_sum = right + picked[1]
                
            if left_sum > right_sum: 
                memo[bound[0], bound[1]] = (bound[0], left_sum)
                return bound[0], left_sum
            
            else:
                memo[bound[0], bound[1]] = (bound[1]-1, right_sum)
                return bound[1]-1, right_sum
                 
        final = pick(0, len(nums))[1]
        return final >= total - final