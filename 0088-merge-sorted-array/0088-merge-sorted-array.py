class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = m - 1
        pointer2 = n - 1
        last = m + n - 1
        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] >= nums2[pointer2]:
                nums1[last] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[last] = nums2[pointer2]
                pointer2 -= 1
            last -= 1
        if pointer1 < 0:
            nums1[:last+1] = nums2[:pointer2+1]