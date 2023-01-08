class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = list(map(sorted,strs))
        res = defaultdict(list)
        for i in range(len(temp)):
            temp[i] = "".join(temp[i])
            res[temp[i]].append(strs[i])
        
        return list(res.values())