class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        def isPeak(idx):
            if arr[idx] > arr[idx-1] and arr[idx] > arr[idx+1]:
                return True
            
            
        left, right = 0, len(arr) - 1
        
        while 1:
            mid = (left+right) // 2
            
            if isPeak(mid):
                return mid
            
            elif arr[mid-1] < arr[mid]:
                left = mid 
                
            elif arr[mid+1] < arr[mid]:
                right = mid