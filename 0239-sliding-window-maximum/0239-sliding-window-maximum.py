class SegmentTree:
    def __init__(self, arr):
        self.size = len(arr)
        self.tree = [0]*self.size + arr
 
        for i in range(self.size-1, 0, -1):
            self.tree[i] = self._combine(self.tree[2*i], self.tree[2*i + 1])

    def _combine(self, a, b):
        return max(a, b)  

    def update(self, index, value):
        index += self.size
        self.tree[index] += value
        while index > 1:
            index //= 2
            self.tree[index] = self._combine(self.tree[2*index], self.tree[2*index + 1])

    def query(self, left, right):
        left += self.size
        right += self.size
        result = self._neutral_element()

        while left <= right:
            if left % 2 == 1:
                result = self._combine(result, self.tree[left])
                left += 1
            if right % 2 == 0:
                result = self._combine(result, self.tree[right])
                right -= 1

            left //= 2
            right //= 2

        return result

    def _neutral_element(self):
        return -float("inf")

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s_tree = SegmentTree(nums)
        ans = []
        
        for idx in range(len(nums) - k + 1):
            ans.append(s_tree.query(idx, idx + k - 1))
            
        return ans