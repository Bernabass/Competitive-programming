class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        occurence = Counter(tasks)
        minn = float(inf)
        maxx = count = 0
        possible_ans = defaultdict(int)
        possible_ans = {2:1,3:1,4:2}
        for i in occurence.values():
            minn = min(minn,i)
            maxx = max(maxx,i)
        
        if minn < 2:
            return -1
    
        for j in range(5,maxx + 1):
            possible_ans[j] = min(possible_ans[j-2],possible_ans[j-3]) + 1
            
        for rep in occurence.values():
            count += possible_ans[rep]

        return count