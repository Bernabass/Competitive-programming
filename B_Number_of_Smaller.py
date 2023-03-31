n2, n1 = map(int, input().split())
arr2, arr1 = list(map(int, input().split())), list(map(int, input().split()))
No_of_greaters = ptr1 = ptr2 = 0
result = [0] * n1

while ptr1 < n1:
    if ptr2 < n2 and arr2[ptr2] < arr1[ptr1]:
        No_of_greaters += 1
        ptr2 += 1
        
    else:
        result[ptr1] += No_of_greaters
        ptr1 += 1
        
print(" ".join(map(str,result)))