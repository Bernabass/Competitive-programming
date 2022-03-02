def max_dom(M,N):
    if M%2==0 or N%2==0:
        return int((M*N)/2)
    else:
        return int(((M*(N+1))/2)-(1+((M-1)/2)))
dimensions=input()
dimensions=dimensions.split()
M,N=int(dimensions[0]),int(dimensions[1])
print(max_dom(M,N))