class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        count = [0]
        for i in range(len(nums1)):
            nums1[i] = nums1[i] - nums2[i]
        
        def merge_sort(arr):
            if len(arr) == 1:
                return arr
            
            mid = len(arr)//2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            compute_pairs(left, right)
            
            return merge(left, right)
        
        def merge(arr1, arr2):
            n1, n2 = len(arr1), len(arr2)
            ptr1 = ptr2 = 0
            result = []

            while ptr1 < n1 and ptr2 < n2:
                if arr1[ptr1] <= arr2[ptr2]:
                    result.append(arr1[ptr1])
                    ptr1 += 1

                else:
                    result.append(arr2[ptr2])
                    ptr2 += 1

            result.extend(arr1[ptr1:])
            result.extend(arr2[ptr2:])

            return result
        
        def compute_pairs(arr1, arr2):
            n1, n2 = len(arr1), len(arr2)
            ptr1 = ptr2 = 0
            
            while ptr1 < n1 and ptr2 < n2:
                if arr1[ptr1] - arr2[ptr2] <= diff:
                    count[0] += n2 - ptr2
                    ptr1 += 1
                    
                else:
                    ptr2 += 1
                
                
        merge_sort(nums1)
        
        return count[0]   