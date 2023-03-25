t = int(input())

for _ in range(t):
    n = int(input())
    leaves = list(map(int,input().split()))
    original = leaves.copy()
    level = 1
    oper = 0
    
    while 2**level <= n:
        gap = 2**level
        ptr1 = 0
        ptr2 = ptr1 + gap - 1
        next_level = []
        
        while ptr2 < n:
            if leaves[ptr1] > leaves[ptr2]:
                prev_gap = gap//2
                first = leaves[ptr1:ptr1+prev_gap]
                second = leaves[ptr1+prev_gap:ptr2+1]
                next_level.extend(second)
                next_level.extend(first)
                
                oper += 1
            else:
                next_level.extend(leaves[ptr1:ptr2+1])
                
            ptr1 += gap
            ptr2 += gap
            
        leaves = next_level
        level += 1
        
    if sorted(original) == leaves:
        print(oper)
        
    else:
        print(-1)
