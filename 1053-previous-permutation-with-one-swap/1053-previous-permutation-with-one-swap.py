class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        prev_arr = []
        ind_hash = defaultdict(int)
        
        for i in range(len(arr) - 1, -1, -1):
            ind = bisect.bisect_left(prev_arr, arr[i])
            if ind != 0:
                var = ind_hash[prev_arr[ind - 1]] 
                arr[i], arr[var] = arr[var], arr[i]
                break
                
            bisect.insort(prev_arr, arr[i])
            ind_hash[arr[i]] = i
            
        return arr
            
            
            
        
        