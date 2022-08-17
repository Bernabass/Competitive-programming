arr=[5,7,7,8,8,10]
target=13
def find(A, target,position):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low+ high) // 2
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid-1
        else:
            if position=='left':
                if mid - 1 < 0:
                    return mid
                if A[mid-1] != target:
                    return mid
                high = mid - 1
            elif position=='right':
                if mid + 1 >=len(A):
                    return mid
                if A[mid+1] != target:
                    return mid
                low = mid+1
    return None
first=find(arr, target,"left")
last=find(arr, target,"right")
if first==None:
    print([-1,-1])
elif first==last:
    print([first,first])
else:
    print([first,last])
