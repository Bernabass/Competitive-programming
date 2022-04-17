nums = [3,30,34,5,9]
a=list(''.join(str(i) for i in nums))
for i in range(len(a)):
    m=a[i]
    for j in range(i,len(a)):
        if a[j]>=m:
            m=a[j]
            idx=j
    a[idx]=a[i]
    a[i]=m
a=''.join(str(i) for i in a)
print(a)
