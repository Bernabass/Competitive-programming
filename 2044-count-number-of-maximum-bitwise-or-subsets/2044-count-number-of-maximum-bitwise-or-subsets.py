class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_OR, count = nums[0], [0]
        ans, n = [], len(nums)
        
        for i in range(1, n):
            max_OR |= nums[i]
        
        def back_track(idx, prev):
            if idx == n:
                return
            
            for i in range(idx, n):
                temp = prev
                prev |= nums[i]
                
                if prev == max_OR:
                    count[0] += 1
                    
                back_track(i+1, prev)
                
                prev = temp
                   
            return
        
        back_track(0, 0)
        
        return count[0]