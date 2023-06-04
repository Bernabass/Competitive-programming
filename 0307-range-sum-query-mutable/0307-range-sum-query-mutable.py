class SegmentTree:
    def __init__(self, arr):
        self.size = len(arr)
        self.tree = [0]*self.size + arr
 
        for i in range(self.size-1, 0, -1):
            self.tree[i] = self._combine(self.tree[2*i], self.tree[2*i + 1])

    def _combine(self, a, b):
        return a+b

    def update(self, index, value):
        index += self.size
        self.tree[index] = value
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

        return result

    def _neutral_element(self):
        return 0
class NumArray:

    def __init__(self, nums: List[int]):
        self.s_tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.s_tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.s_tree.query(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)