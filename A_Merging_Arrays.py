n, m = map(int, input().split())
arr1, arr2 = input().split(), input().split()
n1, n2 = len(arr1), len(arr2)
ptr1 = ptr2 = 0
result = []

while ptr1 < n1 and ptr2 < n2:
    if int(arr1[ptr1]) < int(arr2[ptr2]):
        result.append(arr1[ptr1])
        ptr1 += 1
        
    else:
        result.append(arr2[ptr2])
        ptr2 += 1
  
result.extend(arr1[ptr1:])
result.extend(arr2[ptr2:])  
     
print(" ".join(result))
