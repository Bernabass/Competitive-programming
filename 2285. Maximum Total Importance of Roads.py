from collections import Counter
roads = [[0,1]]
n = 5
keys = set()
for i in roads:
    keys.add(i[0])
    keys.add(i[1])
amount = [0]*len(keys)
dic = dict(zip(keys,amount))
for j in roads:
    dic[j[0]] += 1
    dic[j[1]] += 1
values = list(dic.values())
for m in range(len(values)):
    values[m] = ([values[m],m])
values.sort()
values.reverse()
print(values)
for r in range(len(values)):
    values[r][0] = n-r
for p in values:
    p = p.reverse()
values.sort()
values2 = []
for q in values:
    values2.append(q[1])
dic2 = dict(zip(dic.keys(),values2))
res = 0
for x,y in roads:
    print(dic2[x] , dic2[y])
    res += dic2[x] + dic2[y]
print(res)
