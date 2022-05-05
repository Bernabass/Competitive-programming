def binary_search(array,target):
    first=0
    last=len(array)-1
    median=(first+last+1)//2
    while last>=0 and 0<=(median)<=len(array)-1:
        if array[median]>target:
            last=median-1
        elif array[median]<target:
            first=median+1
        else:
            if array[median-1]!=array[-1] and array[median-1]==target:
                first=1
                last=median-1
                if first==last:
                    return (median)
            else:
                return (median)
        median=(first+last+1)//2
    else:
        return (-1)
