class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leader = []
        counts = defaultdict(int)
        max_count = 0
        inputs = zip(persons, times)
        
        for person, time in inputs:
            counts[person] += 1
            
            if counts[person] > max_count:
                max_count += 1
                leaders = [person]
                
            elif counts[person] == max_count:
                leaders.append(person)
                
            self.leader.append(leaders[-1])
        
        

    def q(self, t: int) -> int:
        
        i = bisect.bisect_left(self.times, t)
        
        if i == len(self.times) or self.times[i] > t:
            return self.leader[i-1]
        
        return self.leader[i]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)