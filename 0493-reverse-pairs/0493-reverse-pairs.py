class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = [0]
        def merge_sort(arr):
            if len(arr) ==  1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            count[0] += find_pairs(left, right)
            
            return merge(left, right)
            
            
        def merge(arr1, arr2):
            n1, n2 = len(arr1), len(arr2)
            ptr1 = ptr2 = next_valid = 0
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
        
        def find_pairs(arr1, arr2):
            n1, n2 = len(arr1), len(arr2)
            ptr1 = ptr2 = valids = 0
            
            while ptr1 < n1 and ptr2 < n2:
                
                if arr2[ptr2]*2 < arr1[ptr1]:
                    valids += len(arr1) - ptr1
                    ptr2 += 1
                    
                else:
                    ptr1 += 1
            
            return valids
        
        merge_sort(nums)
        
        return count[0]