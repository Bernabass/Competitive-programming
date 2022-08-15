t = int(input())
while t:
    n = int(input())
    s = input()
    initial = []
    No_of_moves = 0
    for i in range(n):
        if s[i]=='(':
            initial.append(s[i])
        elif len(initial)==0:
            No_of_moves+=1
        else:
            initial.pop(-1)
    t-=1
    print(No_of_moves)