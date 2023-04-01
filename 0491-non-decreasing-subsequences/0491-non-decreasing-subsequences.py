class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        def back_track(start, curr_ans):
            if start == len(nums):
                return
            
            for i in range(start, len(nums)):
                if not curr_ans or nums[i] >= curr_ans[-1] :
                    curr_ans.append(nums[i])

                    if len(curr_ans) >= 2:
                        res.add(tuple(curr_ans))

                    back_track(i+1, curr_ans)
                    curr_ans.pop()
                                  
        back_track(0, [])
        
        return res    