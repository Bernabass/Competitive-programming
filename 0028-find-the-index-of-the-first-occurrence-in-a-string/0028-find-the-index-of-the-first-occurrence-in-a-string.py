class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        arr, target = deque(haystack), deque(needle)
        k, n = len(target), len(arr)
        curr = deque()
        
        if k > n:
            return - 1
        
        for i in range(k):
            curr.append(arr[i])
            
        if curr == target:
            return 0
        
        
        for idx in range(k, n):
            curr.popleft()
            curr.append(arr[idx])
            
            if curr == target:
                return idx - k + 1
            
            
        return -1