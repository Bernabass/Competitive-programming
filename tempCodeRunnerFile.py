
n,m,a=int(input[0]),int(input[1]),int(input[2])
def Flagstones(m,n,a):
    if  m%a==0:
        p1=m//a
    else:
        p1=(m//a)+1
    if n%a==0:
        p2=n//a
    else:
        p2=(n//a)+1
    return p1*p2
print(Flagstones(n,m,a))