class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i + 1]:
                change = bisect.bisect_left(arr, arr[i], i+1, n)
                target = bisect.bisect_left(arr, arr[change-1], i+1, change)
                arr[i], arr[target] = arr[target], arr[i]

                return arr
            
        return arr        