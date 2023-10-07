class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        stack = []
        idx, N = 0, len(intervals)
        a, b = newInterval
        
        while idx < N:
            start, end = intervals[idx]
            if start >= a:
                if stack:
                    x, y = stack.pop()
                    if a > y:
                        stack.append([x, y])
                        stack.append([a, b])
                        
                    else:
                        new_x = min(a, x)
                        new_y = max(b, y)
                        stack.append([new_x, new_y])
                    
                else:
                    stack.append([a, b])
                    
                break
            else:
                stack.append([start, end])
                
            idx += 1
            
                
        if idx == N:
            x, y = stack.pop()
            if a > y:
                stack.append([x, y])
                stack.append([a, b])

            else:
                new_x = min(a, x)
                new_y = max(b, y)
                stack.append([new_x, new_y])
                
        else:
            for i in range(idx, N):
                start, end = intervals[i]
                x, y = stack.pop()
                if start >= x:
                    if start > y:
                        stack.append([x, y])
                        stack.append([start, end])

                    else:
                        new_x = min(start, x)
                        new_y = max(end, y)
                        stack.append([new_x, new_y])

                else:
                    stack.append([start, end])
                    
        return stack