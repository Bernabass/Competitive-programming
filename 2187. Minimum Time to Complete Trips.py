class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def adder(time,num):
            count=0
            for i in range(len(time)):
                count+=(mid//time[i])    
            return count
        low=1
        high=min(time)*totalTrips
        while low<=high:
            mid=(low+high)//2
            if adder(time,mid)>totalTrips:
                high=mid-1
            elif adder(time,mid)<totalTrips:
                low=mid+1
            else:
                if mid-1<=0 or adder(time,mid-1)!=totalTrips :
                    return mid
                high=mid-1 
        return low