class SnapshotArray:
    def __init__(self, length: int):
        self.arr = defaultdict(list)
        self.snapId = 0

    def set(self, index: int, val: int) -> None:        
        self.arr[index].append([self.snapId, val])

    def snap(self) -> int:
        self.snapId += 1
                    
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.arr[index]
        left, right, ans = 0, len(arr) - 1, -1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= snap_id:
                ans = mid
                left = mid + 1
                
            else:
                right = mid - 1
                
        if ans == -1:
            return 0
        
        return arr[ans][1]