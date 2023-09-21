class SegmentTree:
    def __init__(self, arr):
        self.size = len(arr)
        self.tree = [(float("inf"), -1)]*self.size + [(val, i) for i, val in enumerate(arr)]
        
        for i in range(self.size-1, 0, -1):
            self.tree[i] = self._combine(self.tree[2*i], self.tree[2*i + 1])

    def _combine(self, a, b):
        # We compare the values and take the one with the minimum value,
        # if values are same, take the one with the smallest index
        return a if a[0] <= b[0] else b

    def update(self, index, value):
        index += self.size
        self.tree[index] = (value, index - self.size)
        while index > 1:
            index //= 2
            self.tree[index] = self._combine(self.tree[2*index], self.tree[2*index + 1])

    def query(self, left, right):
        left += self.size
        right += self.size
        result = self._neutral_element()  # Initialize with neutral element

        while left <= right:
            if left % 2 == 1:
                result = self._combine(result, self.tree[left])
                left += 1
            if right % 2 == 0:
                result = self._combine(result, self.tree[right])
                right -= 1

            left //= 2
            right //= 2

        return result[1]  # Return index of the minimum

    def _neutral_element(self):
        return (float("inf"), -1)

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        N = len(target)
        s_tree = SegmentTree(target)
        
        def do(left, right, offset):
            if left < 0 or right == N or left > right:
                return 0
            
            idx = s_tree.query(left, right)
            left_subarray = do(left, idx - 1, -target[idx])
            right_subarray = do(idx + 1, right, -target[idx])
            
            return target[idx] + offset + left_subarray + right_subarray
        
        return do(0, N - 1, 0)
        
        """
        
        
        [5, 3, 1, 2, 7], R = 0
        
        [5, 3], R = 1   [2, 7], R = 1
        
        [5], R = 4      [7], R = 3
        
        
        """