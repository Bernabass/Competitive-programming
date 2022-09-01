t=int(input().strip())
for i in range(t):
    n=int(input().strip())
    array= input().strip().split(' ')
    nums = list(map(int,array))
    out= 'YES'
    for i in range(n):
        if i%2==0:
            if nums[i]%2!=nums[0]%2:
                out='NO'
        else:
            if (nums[i]%2)!=nums[1]%2:
                out='NO'
    print(out)