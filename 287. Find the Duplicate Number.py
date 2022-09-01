class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            count=0
            for num in nums:
                if num<=mid:
                    count+=1
            if count>mid:
                right=mid-1
            else:
                left=mid + 1
        return left