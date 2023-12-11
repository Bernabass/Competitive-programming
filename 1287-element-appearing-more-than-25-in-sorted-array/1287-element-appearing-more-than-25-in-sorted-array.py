class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        N = len(arr)
        freq = Counter(arr)

        for key, val in freq.items():
            if val / N > 0.25:
                return key
