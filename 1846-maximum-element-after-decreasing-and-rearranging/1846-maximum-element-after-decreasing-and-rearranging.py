class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        freq = Counter(arr)
        can_change = 0
        n = ans = len(arr)
        for num in arr:
            if num > n:
                can_change += 1
        
        for i in range(n, 0, -1):
            if not freq[i]:
                if can_change: 
                    can_change -= 1               
                else: 
                    ans -= 1

            else:
                can_change += freq[i] - 1
            
        return ans