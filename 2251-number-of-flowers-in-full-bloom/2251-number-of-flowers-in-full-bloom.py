class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        arr = flowers.copy()
        flowers.sort()
        flowers = [a for a, b in flowers]
        arr.sort(key = lambda x:x[1])
        arr = [b for a, b in arr]
        N = len(arr)
        
        ans = [0] * len(people)        
        for idx, day in enumerate(people):
            started = bisect_right(flowers, day)
            started += (flowers[started] == day) if started < N else 0
            ended = bisect_left(arr,  day)
            
            ans[idx] = started - ended 
            
        return ans