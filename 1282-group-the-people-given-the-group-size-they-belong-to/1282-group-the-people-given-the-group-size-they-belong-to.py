class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        ans = []
        
        for person, max_members in enumerate(groupSizes):
            groups[max_members].append(person)
            
            if len(groups[max_members]) == max_members:
                ans.append(groups[max_members])
                groups[max_members] = []
                
        return ans