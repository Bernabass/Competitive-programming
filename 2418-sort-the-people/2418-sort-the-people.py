class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(n):
            minn = i
            for j in range(i,n):
                if heights[j] > heights[minn]:
                    minn = j
                    
            heights[i], heights[minn] = heights[minn], heights[i]
            names[i], names[minn] = names[minn], names[i]
            
        return names