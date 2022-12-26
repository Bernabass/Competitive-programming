n = int(input())
members = input().split()
flags = set(input().split())
count = 0
for stud in members:
    if stud not in flags:
        temp = stud.count(stud[0])
        for char in stud:
            if stud.count(char) != temp:
                break
        else:
            count += 1
print(count)