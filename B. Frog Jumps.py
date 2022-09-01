n = int(input())
while n>0:
    array=input()
    i=0
    j=0
    for k in range(len(array)):
        if array[k]=='L':
            i+=1
        else:
            if i>j:
                j=i
            i=0
        if i>j:
            j=i
    print(j+1)
    n-=1