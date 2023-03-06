class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = [-1]*len(nums2)
        n1, n2 = len(nums1), len(nums2)
        stack = [nums2[-1]]
        
        for i in range(n2 - 2, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if stack:
                next_greater[i] = stack[-1]
                
            stack.append(nums2[i])
                    
                    
        info = dict(zip(nums2, next_greater))
                    
        for idx, val in enumerate(nums1):
            nums1[idx] = info[val]
            
        return nums1
        