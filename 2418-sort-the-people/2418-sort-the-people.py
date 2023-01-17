class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = list(zip(heights,names))
        res.sort(reverse=True)
        ans = []
        for name in res:
            ans.append(name[1])
            
        return ans