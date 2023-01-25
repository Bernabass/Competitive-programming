class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniques = list(set(nums))
        uniques.sort()
        for i in range(len(uniques)):
            nums[i] = uniques[i]
            
        return len(uniques)