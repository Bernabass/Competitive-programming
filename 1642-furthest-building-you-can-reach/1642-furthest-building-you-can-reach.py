class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        idx, n = 0, len(heights)
        
        while idx < n - 1:
            curr_height, next_height = heights[idx], heights[idx+1]
            
            if next_height > curr_height:
                diff = next_height - curr_height
                
                if bricks >= diff:
                    heappush(heap, -diff)
                    bricks -= diff
                    idx += 1
                    
                elif ladders:
                    if heap:
                        prev_max = abs(heappop(heap))
                        if diff < prev_max:
                            bricks += prev_max

                        else:
                            heappush(heap, -prev_max)
                            idx += 1
                    else:
                        idx += 1
                        
                    ladders -= 1  
                else:
                    break
                    
            else:
                idx += 1
                    
        return idx