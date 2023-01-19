class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n, mountain = len(arr), False
        for i in range(1,n-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                mountain = True
                
            elif arr[i-1] >= arr[i] <= arr[i+1]:
                return False
            
        return mountain