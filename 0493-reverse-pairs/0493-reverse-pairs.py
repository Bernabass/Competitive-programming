class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = [0]
        def divide(arr):
            if len(arr) ==  1:
                return arr
            
            mid = len(arr) // 2
            left = divide(arr[:mid])
            right = divide(arr[mid:])
            
            start = 0
            end = len(right) - 1
            for num in left:
                res = search(right, start, end, num)
                count[0] += res
                start = res
                if res > 0:
                    start = res - 1
            
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
        
        def search(arr, left, right, target):
            org = left
            while left <= right:

                mid = (left+right) // 2
                if mid >= len(arr):
                    break
                if arr[mid]*2 < target:
                    if mid+1 == len(arr):
                        return mid+1
                    if arr[mid+1]*2 >= target:
                        return mid+1

                    left = mid+1

                else:
                    right = mid - 1

            return org
        
        divide(nums)
        return count[0]