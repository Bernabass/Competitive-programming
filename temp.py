nums =[3,1]
target=1
low=0
high=len(nums)-1
zeroth=nums[0]
while low<high:
    mid=(low+high)//2
    if nums[mid]>=zeroth:
        low=mid+1
    else:
        high=mid
print(low)
def binary_search(arr, x,left,right):
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            return mid
    return -1
if nums[low]<zeroth:
    if zeroth<=target<=nums[low-1]:
        print(binary_search(nums,target,0,low-1))
        exit()
    else:
        print(binary_search(nums,target,low,len(nums)-1))
        exit()
else:
    print(binary_search(nums,target,0,len(nums)-1))
