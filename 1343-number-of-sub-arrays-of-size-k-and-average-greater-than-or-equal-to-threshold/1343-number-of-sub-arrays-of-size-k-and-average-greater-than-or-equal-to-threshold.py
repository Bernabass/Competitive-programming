class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n, count = len(arr), 0
        window_sum = sum(arr[:k])
        
        if window_sum / k >= threshold:
            count += 1
            
        for idx in range(k,n):
            window_sum -= arr[idx-k]
            window_sum += arr[idx]
            
            if window_sum / k >= threshold:
                count += 1
                
        return count    