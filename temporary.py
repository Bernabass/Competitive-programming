import math
nums = [44,22,33,11,1]
threshold = 5
test_cases=list(range(1,max(nums)+1))
low=0
high=len(test_cases) - 1
while low<=high:
    mid=(low+ high)//2
    result=0
    for i in nums:
        result+=math.ceil(i/(test_cases[mid]))
    if low==high:
        print(test_cases[mid])
        break
    if result > threshold:
        low=mid + 1
    else:
        if mid-1 < 0:
            print(test_cases[mid])
            break
        result=0
        for i in nums:
            result+=math.ceil(i/(test_cases[mid-1]))
        if result>threshold:
            print(print(test_cases[mid]))
            break
        high = mid-1