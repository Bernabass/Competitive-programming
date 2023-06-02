class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x:x[1])
        heap, curr_time = [], 0
        
        for duration, last_day in courses:
            if curr_time + duration <= last_day:
                heappush(heap, -duration)
                curr_time += duration
            elif heap and -heap[0] > duration:
                curr_time += heappop(heap) + duration
                heappush(heap, -duration)
                
        return len(heap)