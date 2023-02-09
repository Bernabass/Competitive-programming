class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        info = dict(zip(numbers,range(len(numbers))))
        for idx, num in enumerate(numbers):
            if target - num in info:
                return [idx+1, info[target-num] + 1]