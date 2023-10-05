class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        def find(arr, k):
            freq = Counter(arr)
            
            for num in arr:
                freq[num] += 1
                
                if len(freq) == k:
                    freq -= Counter(set(freq))
                    
            return [num for num in freq if nums.count(num) > len(nums) // k]
        
        return find(nums, 3)