class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def time(s, v):
            return (target - s) / v
        
        info = list(zip(position, speed))
        info.sort()
        durations = []
        for data in info:
            durations.append(time(data[0], data[1]))
          
        for i in range(1, len(durations)):
            if durations[i] > durations[i-1]:
                durations[i-1] = durations[i]
                
        stack = []
        for i in range(len(durations)-1, -1, -1):
            while stack and durations[stack[-1]] > durations[i]:
                durations[i] = durations[stack[-1]] 

            stack.append(i)
          
        return len(set(durations))
        
        