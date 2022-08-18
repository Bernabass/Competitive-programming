citations = [0,1,3,5,6]
low=0
high = len(citations) - 1
while low <= high:
    mid = (low+ high) // 2
    if low==high and citations[mid] >=len(citations)-mid:
        print(len(citations)-mid)
        break    
    if citations[mid] >=len(citations)-mid:
        if mid - 1 < 0:
            print(len(citations)-mid)
            break
        if citations[mid-1] < (len(citations)-mid+1):
            print(len(citations)-mid)
            break
        high = mid - 1      
    else:
        low = mid+1
else:
    print(0)
    
