class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        info = defaultdict(list)
        
        for num in nums:
            if not info[num-1]:
                heappush(info[num], 1)
                
            else:
                min_arr = heappop(info[num-1])
                heappush(info[num], min_arr+1)
                
                
        for val in info.values():
            if val and heappop(val) < 3:
                return False
            
        return True