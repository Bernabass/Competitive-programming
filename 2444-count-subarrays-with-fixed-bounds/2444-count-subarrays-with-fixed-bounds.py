class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        if minK > maxK: 
            return 0
        
        def count(l, r):
            if l + 1 == r: 
                return 0
            info = Counter([nums[l]])
            ans, j = 0, l + 1
            for i in range(l + 1, r):
                info[nums[i - 1]] -= 1
                while not info[minK] * info[maxK] and j < r:
                    info[nums[j]] += 1
                    j += 1
                if info[minK] * info[maxK]: ans += r - j + 1
                else: 
                    break
            return ans
        
        arr = [-1] + [i for i, num in enumerate(nums) if num < minK or num > maxK] + [len(nums)]
        return sum(count(arr[i - 1], arr[i]) for i in range(1, len(arr)))