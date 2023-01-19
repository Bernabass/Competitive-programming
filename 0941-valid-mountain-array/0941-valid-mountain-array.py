class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        
        count = -1
        for i in range(1,n-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                count += 1
                
            elif arr[i] <= arr[i-1] and arr[i] <= arr[i+1]:
                return False
            
        return not count