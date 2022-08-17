class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(nums, target,position):
            low=0
            high=len(nums) - 1
            while low<=high:
                mid=(low+ high)//2
                if nums[mid]<target:
                    low=mid + 1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    if position=='left':
                        if mid-1 < 0:
                            return mid
                        if nums[mid-1]!=target:
                            return mid
                        high = mid-1
                    elif position=='right':
                        if mid + 1 >=len(nums):
                            return mid
                        if nums[mid+1] != target:
                            return mid
                        low = mid+1
            return None
        first=find(nums, target,"left")
        last=find(nums, target,"right")
        if first==None:
            return ([-1,-1])
        elif first==last:
            return ([first,first])
        else:
            return ([first,last])        