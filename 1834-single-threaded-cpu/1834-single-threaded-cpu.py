class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [tasks[i] + [i] for i in range(len(tasks))]
        heapify(tasks)
        start, end, org_idx = heappop(tasks)
        ans, availables = [org_idx], []
        limit = start + end
        
        while tasks:
            while tasks and tasks[0][0] <= limit:
                start, end, org_idx = heappop(tasks)
                heappush(availables, (end, org_idx, start))
            
            if not availables:
                start, end, org_idx = heappop(tasks)
                ans.append(org_idx)
                limit = start + end
                
            else:
                end, org_idx, start = heappop(availables)
                ans.append(org_idx)
                limit += end
            
        while availables:
            _, org_idx, _ = heappop(availables)
            ans.append(org_idx)
            
        return ans