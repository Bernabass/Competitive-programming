time =[1]
totalTrips = 4
def adder(time,num):
    count=0
    for i in range(len(time)):
        count+=(num//time[i])    
    return count
low=1
high=sum(time)+totalTrips
while low<=high:
    mid=(low+high)//2
    if adder(time,mid)>totalTrips:
        high=mid-1
    elif adder(time,mid)<totalTrips:
        low=mid+1
    else:
        if mid-1<=0:
            print(mid)
            break
        if adder(time,mid-1)!=totalTrips:
            print(mid)
            break
        high=mid-1
else:
    print(low)