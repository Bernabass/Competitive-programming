weights = [1,2,3,1,1]
days = 4
capacities=list(range(max(weights),sum(weights)+1))
def ispossible(weights,min_weight):
    original=weights.copy()
    weights.reverse()
    count=0
    day=0
    while len(weights)>=0:
        if len(weights)==0:
            day+=1
            count=0
            break
        elif weights[-1]+count>min_weight:
            day+=1
            count=0            
        else:
            count+=weights.pop()
        print(weights,day)
    weights.extend(original)
    return day
print(ispossible(weights,3))
# low=0
# high=len(capacities) - 1
# while low<=high:
#     mid=(low+ high)//2
#     if ispossible(weights,capacities[mid])>days:
#         low=mid + 1
#     elif ispossible(weights,capacities[mid])<days:
#         high=mid-1
#     else:
#         if mid-1 < 0 or ispossible(weights,capacities[mid-1])!=days :
#             print(capacities[mid])
#             break
#         high = mid-1