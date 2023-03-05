class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        max_to = float("-inf")
        for trip in trips:
            max_to = max(max_to, trip[2])
            
        arr = [0]*(max_to + 1)
        for trip in trips:
            left, right = trip[1], trip[2]
            val = trip[0]
            
            arr[left] += val
            arr[right] -= val
          

        curr_max_passenger = prefix_sum = 0
        for num in arr:
            prefix_sum += num
            curr_max_passenger = max(curr_max_passenger, prefix_sum)
            
        return curr_max_passenger <= capacity
        
        