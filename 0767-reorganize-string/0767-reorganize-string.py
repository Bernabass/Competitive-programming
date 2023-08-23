class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        heap, ans = [], []
        
        for char, count in freq.items():
            heappush(heap, (-count, char))
            
        while heap:
            curr_count, curr_char = heappop(heap)
            curr_count *= -1
            if heap:
                next_count, next_char = heappop(heap)
                next_count *= -1
                ans.extend([curr_char, next_char])
                
                if curr_count - 1:
                    heappush(heap, (-(curr_count - 1), curr_char))
                    
                if next_count - 1:
                    heappush(heap, (-(next_count - 1), next_char))
                
            else:
                if curr_count > 1:
                    return ""
                
                else:
                    ans.append(curr_char)
                    break
            
        return "".join(ans)