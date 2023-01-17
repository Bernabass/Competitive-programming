class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(n):
            minn = [-float("inf"),i]
            for j in range(i,n):
                if heights[j] > minn[0]:
                    minn = [heights[j],j]
                    
            heights[i], heights[minn[1]] = heights[minn[1]], heights[i]
            names[i], names[minn[1]] = names[minn[1]], names[i]
            
        return names