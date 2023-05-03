class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr1, arr2 = set(nums1), set(nums2)
        
        return [list(arr1 - arr2), list(arr2 - arr1)]