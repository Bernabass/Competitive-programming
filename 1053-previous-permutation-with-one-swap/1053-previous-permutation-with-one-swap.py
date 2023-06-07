class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        ind = len(arr)
        
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                ind = i
                break
        if ind == len(arr):
            return arr
        
        change = ind + 1
        prev = arr[ind + 1]
        for i in range(ind + 1, len(arr)):
            if arr[i] > prev and arr[i] < arr[ind]:
                change = i
                
        arr[ind], arr[change] = arr[change], arr[ind]
                
        return arr