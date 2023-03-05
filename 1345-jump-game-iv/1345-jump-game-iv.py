class Solution:
    def minJumps(self, arr: List[int]) -> int:
        info = defaultdict(list)
        for idx, val in enumerate(arr): 
            info[val].append(idx)
            
        
        seen, queue = {0}, deque([0])
        min_steps = 0
        while queue: 
            for _ in range(len(queue)): 
                
                i = queue.popleft()
                if i+1 == len(arr): 
                    return min_steps 
                
                for j in [i-1, i+1] + info[arr[i]]: 
                    if 0 <= j < len(arr) and j not in seen: 
                        seen.add(j)
                        queue.append(j)
                        
                info.pop(arr[i])
                
            min_steps += 1