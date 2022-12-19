# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
k = int(input())
rooms = input()
rooms = rooms.split()
col = Counter(rooms)
for i in col:
    if col[i] == 1:
        print(i)
        break