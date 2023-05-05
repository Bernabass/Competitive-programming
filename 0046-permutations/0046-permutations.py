class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def insert(num, arr):
            total = []

            for curr in arr:
                n = len(curr)+1
                for count in range(n):
                    ans, idx = [11]*n, 0
                    ans[count] = num
                    
                    for i, val in enumerate(ans):
                        if val == 11:
                            ans[i] = curr[idx]
                            idx += 1
                
                    total.append(ans)
                    
            return total
        
        level = [[nums[0]]]
        
        for i in range(1, len(nums)):
            level = insert(nums[i], level)
            
        return level