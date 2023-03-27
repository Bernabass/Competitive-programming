class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = list(zip(nums, range(len(nums))))
        ans = [0]*len(nums)
        
        def merge_sort(arr):
            if len(arr) == 1:
                return arr
            
            mid = len(arr)//2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            count_smallers(left, right)
            
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
        
        def count_smallers(arr1, arr2):
            n1, n2 = len(arr1), len(arr2)
            prefix_arr = [0] * n1
            ptr1 = ptr2 = 0
            
            while ptr1 < n1 and ptr2 < n2:
                if arr2[ptr2] < arr1[ptr1]:
                    prefix_arr[ptr1] += 1
                    ptr2 += 1
                    
                else:
                    ptr1 += 1
            
            ans[arr1[0][1]] += prefix_arr[0]
            for i in range(1, n1):
                prefix_arr[i] += prefix_arr[i-1]
                ans[arr1[i][1]] += prefix_arr[i]
                
        merge_sort(nums)
                
        return ans