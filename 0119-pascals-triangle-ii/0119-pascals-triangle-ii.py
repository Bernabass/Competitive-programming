class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans, seen = [], defaultdict(int)
        def get_value(row, col):
            if (row, col) in seen:
                return seen[(row, col)]
            if row == col or not col:
                return 1
            
            ans = get_value(row-1, col-1) + get_value(row-1, col)
            seen[(row, col)] += ans
            
            return ans
        
        for i in range(rowIndex+1):
            ans.append(get_value(rowIndex, i))
            
        return ans