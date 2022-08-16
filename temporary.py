from collections import Counter
import heapq
words=["the","day","is","sunny","the","the","the","sunny","is","is"]
k=4
temp=Counter(words)
out=[]
final=[]
print(temp)
for i in temp:
    temp[i]=-temp[i]
    out.append([temp[i],i])
heapq.heapify(out)
print(out)
for j in range(k):
    final.append(heapq.heappop(out)[1])
print(final)