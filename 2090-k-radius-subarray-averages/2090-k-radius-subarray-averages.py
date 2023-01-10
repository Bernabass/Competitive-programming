class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k > n:
            return [-1]*n
        ans = []
        window_size = 2*k + 1
        nums.reverse()
        prev_sum = sum(nums[:window_size])
        ans.append(prev_sum // window_size)
        
        for idx in range(window_size,n):
           curr_sum = prev_sum - nums[idx-window_size] + nums[idx]
           ans.append(curr_sum // window_size)     
           prev_sum = curr_sum
                       
        ans.reverse()
        temp = [-1] * n
        for i in range(k,n-k):
            temp[i] = ans[i-k]
                       
        return temp
                    
                       
                       