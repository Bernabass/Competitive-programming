arr=[2,6,1,5,8,4,9]
n=len(arr)
def heapify(arr,n):
    for i in range((n//2)-1,-1,-1):
        largest=i
        left_child=2*i+1
        right_child=2*i+2
        if left_child < n and arr[left_child]>arr[largest]:
            largest=left_child
        if right_child < n and arr[right_child]>arr[largest]:
            largest=right_child
        arr[i],arr[largest]=arr[largest],arr[i]
        return heapify(arr,i)
    else:
        return arr


print(heapify(arr,n))