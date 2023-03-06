class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low=0
        high = len(citations) - 1
        while low <= high:
            mid = (low+ high) // 2
            if low==high and citations[mid] >=len(citations)-mid:
                return (len(citations)-mid)  
            if citations[mid] >=len(citations)-mid:
                if mid - 1 < 0:
                    return (len(citations)-mid)
                if citations[mid-1] < (len(citations)-mid+1):
                    return (len(citations)-mid)     
                high = mid - 1      
            else:
                low = mid+1
        else:
            return 0