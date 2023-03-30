class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        org = [0]*(2*k + 1)
        limit = [startPos-k, startPos+k]
        offset = startPos - k
        
        for position, amount in fruits:
            if limit[0] <= position <= limit[1]:
                org[position-offset] += amount
                    
        max_harvest = [0]
        prefix_sum = org.copy()

        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i-1]

        def cover(arr, steps, back):
            start = len(arr) // 2
            allowed = steps
            (left, right, idx) = ((steps, 0, steps) if back else (0, steps, steps))
            
            while 0 <= idx < 2*k + 1 and steps >= 0:
                steps = allowed
                if back:
                    steps -= start - left 
                    right = idx = left + steps  
                else:
                    steps -= right - start
                    left = idx = right - steps
                
                max_harvest[0] = max(max_harvest[0], prefix_sum[right]-prefix_sum[left]+org[left])
                left -= back; right += (not back); idx -= (1 if back else -1)
            return
        
        cover(org, k, 1)
        cover(org, k, 0)
        
        return max_harvest[0] 