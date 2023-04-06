class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n=len(nums)
        beg,end=min(nums),max(nums)
        ans=nums[0]
        def check(x):
            c=0
            for i in range(n-1,-1,-1):
                if nums[i]>x:
                    c+=nums[i]-x
                else:
                    if nums[i]+c>x:
                        c=nums[i]+c-x
                    else:
                        c=0
            return c==0
        while beg<=end:
            mid=(beg+end)//2
            if check(mid):
                ans=mid
                end=mid-1
            else:
                beg=mid+1
        return ans
