inp = list(map(int,input().split()))
n , k = inp[0] , inp[1]
lectures = list(map(int,input().split()))
mode = list(map(int,input().split()))
left, right = 0, 0
sleep ,max_sleep = 0 , 0
wake = 0

for _ in range(k):
    if mode[right] == 0:
        sleep += lectures[right]
    else:
        wake += lectures[right]
    right += 1
max_sleep = max(max_sleep,sleep)

while right < n:
    if mode[left] == 0:
        sleep -= lectures[left]

    if mode[right] == 0:
        sleep += lectures[right]
    else:
        wake += lectures[right]
    left += 1
    right += 1
    max_sleep = max(max_sleep,sleep)
    
print(wake + max_sleep)
