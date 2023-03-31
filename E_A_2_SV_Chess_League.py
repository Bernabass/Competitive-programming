round, max_diff = map(int, input().split())
players = list(zip(range(1, (2**round)+1), map(int, input().split())))

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = mergeSort(arr[:mid])
    right_half = mergeSort(arr[mid:])

    return find_winners(left_half, right_half)

def merge(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    ptr1 = ptr2 = 0
    result = []
    
    while ptr1 < n1 and ptr2 < n2:
        if arr1[ptr1][1] <= arr2[ptr2][1]:
            result.append(arr1[ptr1])
            ptr1 += 1
            
        else:
            result.append(arr2[ptr2])
            ptr2 += 1
            
    result.extend(arr1[ptr1:])
    result.extend(arr2[ptr2:])
    
    return result

def find_winners(arr1, arr2):
    i = j = 0
    while i < len(arr1) and j < len(arr2) and abs(arr1[i][1]-arr2[j][1]) > max_diff:
        if arr1[i][1] < arr2[j][1]:
            i += 1
        else:
            j += 1
    
    return merge(arr1[i:], arr2[j:])

res = mergeSort(players)
indices = [sublist[0] for sublist in res]

print(" ".join(map(str, sorted(indices))))