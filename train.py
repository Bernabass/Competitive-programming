def selectionSort(arr,n):
    #code here
    output=[]
    for i in range(n):
        output.append(min(arr))
        arr.remove(min(arr))
    return output
arr=[4,1,3,9,7]
n=5
print(selectionSort(arr,n))