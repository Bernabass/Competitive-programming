class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        limit = float("-inf")
        for req in requests:
            limit = max(limit, req[1])
            
        arr = [0]*(limit+1)
        n = len(arr)
        
        for req in requests:
            left, right = req[0], req[1]
            
            arr[left] += 1
            if right + 1 < n:
                arr[right+1] -= 1
                
                
        for i in range(1, n):
            arr[i] += arr[i-1]
            
        original = arr.copy()
        arr.sort(reverse = True)
        nums.sort(reverse = True)
        info = defaultdict(deque)
        
        for idx, val in enumerate(arr):
            info[val].append(nums[idx])
            
        for idx, val in enumerate(original):
            original[idx] = info[val].popleft()
            
        prefix_sum = [0]
        
        for num in original:
            prefix_sum.append(prefix_sum[-1]+num)
            
        ans = 0
        
        for req in requests:
            left, right = req[0], req[1]
            ans += prefix_sum[right+1] - prefix_sum[left]
            
        return ans % (10**9 + 7)
            
            