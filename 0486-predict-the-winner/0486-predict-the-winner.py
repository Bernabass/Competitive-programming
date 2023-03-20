class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        memo = defaultdict(list)
        
        def pick(start, end):
            
            if start == end:
                return 0, 0
            
            if end - start == 1:
                
                return nums[start], nums[start]
            
            bound = [start, end]
            left = nums[start]
            start += 1
            temp = (start, end)
            
            if temp in memo:
                ptr = memo[temp][0]
                
            else:
                picked = pick(start, end)
                ptr = picked[0]
            
            if start == ptr:
                start += 1
            
            else:
                end -= 1
            
            temp = (start, end)
            if temp in memo:
                left_sum = left + memo[temp][1]
                
            else:
                picked = pick(start, end)
                left_sum = left + picked[1]
             
            start, end = bound
            right = nums[end - 1]
            end -= 1
            temp = (start, end)
            
            if temp in memo:
                ptr = memo[temp][0]
                
            else:
                picked = pick(start, end)
                ptr = picked[0]
            
            if start == ptr:
                start += 1
            
            else:
                end -= 1
            
            temp = (start, end)
            if temp in memo:
                right_sum = right + memo[temp][1]
                
            else:
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