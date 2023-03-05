class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        limit = float("-inf")
        for req in requests:
            limit = max(limit, req[1])
         
        
        arr = [0]*(limit+2)
        n = len(arr) - 1
        for req in requests:
            left, right = req[0], req[1]
            
            arr[left] += 1
            arr[right+1] -= 1
                    
        for i in range(1, n):
            arr[i] += arr[i-1]
          
        arr.sort(reverse = True)
        nums.sort(reverse = True)
        ans = 0
        
        for idx in range(n):
            ans += arr[idx] * nums[idx]
            
        return ans % (10**9 + 7)        