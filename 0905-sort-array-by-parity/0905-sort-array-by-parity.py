class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr = deque()
        
        for num in nums:
            if num % 2:
                arr.append(num)
                
            else:
                arr.appendleft(num)
                
        return arr