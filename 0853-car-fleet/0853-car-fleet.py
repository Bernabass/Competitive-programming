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
                
        previous_greater = durations[-1]
        for i in range(len(durations)-2, -1, -1):
            if durations[i] < previous_greater:
                durations[i] = previous_greater
                
            else:
                previous_greater = durations[i]
          
        return len(set(durations))  
        
        