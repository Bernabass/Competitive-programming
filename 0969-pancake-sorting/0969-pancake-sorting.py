class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        sorted_arr = arr.copy()
        n = len(arr)
        sorted_arr.sort(reverse = True)
        res = []
        for i in sorted_arr:
            k = arr.index(i)
            temp = arr[:k+1]
            temp.reverse()
            temp.extend(arr[k+1:])
            temp.reverse()
            
            res.extend([k+1,n])
            arr = temp[:len(temp)-1]
            n -= 1
            
            
        return res