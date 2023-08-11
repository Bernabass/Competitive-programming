class Solution:
    def trap(self, height: List[int]) -> int:
        n, total_area = len(height), 0
        prefix_max = defaultdict(int)
        suffix_max = defaultdict(int)
        
        prefix_max[0] = height[0]
        for idx in range(1, n):
            prefix_max[idx] = max(prefix_max[idx - 1], height[idx])
        
        suffix_max[n - 1] = height[n - 1]
        for idx in range(n - 2, -1, -1):
            suffix_max[idx] = max(suffix_max[idx + 1], height[idx])
        
        for idx in range(n):
            total_area += min(prefix_max[idx], suffix_max[idx]) - height[idx]
            
        return total_area