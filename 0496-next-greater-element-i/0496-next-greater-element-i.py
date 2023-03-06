class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [nums2[0]]
        next_greater = {}
        
        for idx, curr_element in enumerate(nums2, 1):  
            while stack and curr_element > stack[-1]:
                next_greater[stack.pop()] = curr_element
                
            stack.append(curr_element)
            
        for idx, num in enumerate(nums1):
            if num in next_greater:
                nums1[idx] = next_greater[num]
                
            else:
                nums1[idx] = -1
                
        return nums1