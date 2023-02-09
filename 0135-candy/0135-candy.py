class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        mandatory = [1]*n
        arranged = ratings.copy()
        arranged.sort()
        info = defaultdict(deque)
        
        for idx, val in enumerate(ratings):
            info[val].append(idx)
            

        for idx, val in enumerate(arranged):
            index = info[val].popleft()
            possible_ans = []
            
            if (index - 1) >= 0 and ratings[index - 1] < ratings[index]:
                possible_ans.append(mandatory[index - 1])
            

            if (index + 1) < n and ratings[index + 1] < ratings[index]:

                possible_ans.append(mandatory[index + 1])
                

            if possible_ans:
                mandatory[index] = max(possible_ans) + 1
                
                
                
        return sum(mandatory)      