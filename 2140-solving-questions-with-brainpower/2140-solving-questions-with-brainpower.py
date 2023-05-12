class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        info, n = defaultdict(int), len(questions)
        
        for i in range(n-1, -1, -1):
            info[i] = max(info[i+questions[i][1]+1] + questions[i][0], info[i+1])
            
        return info[0]