class SegmentTree:
    def __init__(self, arr):
        self.size = len(arr)
        self.tree = [0]*self.size + arr
 
        for i in range(self.size-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]

    def update(self, index, value):
        index += self.size
        self.tree[index] += value
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[2*index] + self.tree[2*index + 1]

    def query(self, left, right):
        left += self.size
        right += self.size
        result = 0

        while left <= right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 0:
                result += self.tree[right]
                right -= 1

            left //= 2
            right //= 2

        return result

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sums = []
        prev_sum = ans = 0
        
        for val in nums:
            prev_sum += val

            if lower <= prev_sum <= upper:
                ans += 1
                
            left_index = bisect.bisect_left(prefix_sums, prev_sum - upper)
            right_index = bisect.bisect_right(prefix_sums, prev_sum - lower)
            
            ans += right_index - left_index
            bisect.insort(prefix_sums, prev_sum)
            
        return ans