n,m=map(int,input().split())
push=0
while n<m:
    if m%2!=0:
        m+=1
        push+=1
    else:
        m/=2
        push+=1
print(int(push+n-m))


# n,m=map(int,input().split())
# push=0
# while n is not m:
#     if n>m:
#         m+=1
#     elif n<m:
#         if m%2==0:
#             m=m//2
#         else:
#             m+=1
#     push+=1
# print(push)

# n,m=map(int,input().split())
# if n >= m: 
#     print(n-m)
# else:
#     push=0

#     while n is not m:
#         if abs(m-2*(n-1))<=abs(m-2*n):
#             n-= 1 
#         else:
#             n=2*n
#         push+= 1
#     print(push)