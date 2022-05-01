class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output=[]
        for i in nums1:
            a=nums2.index(i)
            for j in nums2[a+1:]:
                if j>i:
                    output.append(j)
                    break
                else:
                    continue
            else:
                output.append(-1)
        return output
        