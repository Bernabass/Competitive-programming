class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n, res = len(nums), set()
        
        def back_track(start, curr_ans, prev):
            if start == n:
                return
            
            for i in range(start, n):
                if nums[i] >= prev:
                    curr_ans.append(nums[i])

                    if len(curr_ans) >= 2:
                        res.add(tuple(curr_ans.copy()))

                    back_track(i+1, curr_ans, nums[i])
                    curr_ans.pop()
                                  
        back_track(0, [], -101)
        
        return res    