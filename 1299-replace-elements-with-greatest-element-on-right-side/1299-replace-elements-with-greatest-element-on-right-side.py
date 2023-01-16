class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        greatest = arr[-1]
        arr[-1] = -1
        for idx in range(n-2,-1,-1):
            curr = arr[idx]
            arr[idx] = greatest
            greatest = max(greatest,curr)
            
        return arr