from collections import Counter
import heapq
import math

matrix=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
k=5
out=[]
for i in matrix:
    out=[*out,*i]
heapq.heapify(out)
for i in range(k-1):
    heapq.heappop(out)
print(out[0])
print(sorted(out)[k-1])
# n=len(matrix)
# current_row=math.ceil(k/n)
# temp=[]
# temp.extend(matrix[current_row-1])
# initial_idx=(current_row-1)*n
# if current_row>1:
#     initial_idx=(current_row-2)*n
#     temp.extend(matrix[current_row-2])
# if current_row<n:
#     temp.extend(matrix[current_row])
# print(temp)
# heapq.heapify(temp)
# for i in range(k-initial_idx-1):
#     heapq.heappop(temp)
# print(temp[0])

