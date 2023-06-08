class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        n=len(grid[0])
        for i in grid:
            low=0
            high=n-1
            while low<=high:
                mid=(low+high)//2
                if high==low==mid and i[mid]<0:
                    count+=n-mid
                    break
                elif i[mid]>=0:
                    low=mid+1
                else:
                    high=mid
            low=0
            high=n-1
        return count
        