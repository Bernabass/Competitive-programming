class my_dict(defaultdict):
    def __missing__(self, key):
        return (0, 0)

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        info = my_dict()
        ans, curr_max = [], 0
        
        while removeQueries:
            idx = removeQueries.pop()
            info[idx] = (nums[idx], 1)
            r_idx, r_len = info[idx+1]
            l_idx, l_len = info[idx-1]
            
            curr_sum = nums[idx] + r_idx + l_idx
            info[idx+r_len] = (curr_sum, l_len + r_len + 1)
            info[idx-l_len] = (curr_sum, l_len + r_len + 1)
            
            ans.append(curr_max)
            curr_max = max(curr_max, curr_sum)
         
        ans.reverse()
        
        return ans