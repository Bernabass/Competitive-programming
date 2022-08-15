n,m = map(int, input().split())
list_of_rooms= list(map(int, input().split()))
list_of_roomNo = list(map(int, input().split()))
temp=0
f=0
for i in list_of_roomNo:
    while i > temp:
        temp+= list_of_rooms[f]
        f+=1
    k=i-(temp - list_of_rooms[f-1])
    print(f,k)