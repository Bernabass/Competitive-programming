class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        left = 0
        right = len(colors) - 1
        
        while left <= right:
            if colors[left] != colors[right]:
                maxx = right - left
                break
            
            right -= 1
        left = 0
        right = len(colors) - 1
        while left <= right:
            if colors[left] != colors[right]:
                return max(maxx,right - left)
            
            left += 1