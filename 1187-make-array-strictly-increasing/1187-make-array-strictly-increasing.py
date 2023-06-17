class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
            info = {-1:0}
            arr2.sort()
            for i in arr1:
                curr = defaultdict(lambda: float('inf'))
                for key in info:
                    if i > key:
                        curr[i] = min(curr[i],info[key])
                    pos = bisect.bisect_right(arr2,key)
                    if pos < len(arr2):
                        curr[arr2[pos]] = min(curr[arr2[pos]], info[key]+1)
                info = curr
                
            if info:
                return min(info.values())
            
            return -1