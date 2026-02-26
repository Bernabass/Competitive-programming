I=input
for _ in"L"*int(I()):
 n,x,k=map(int,I().split());i=p=0;j=m=k
 for c in I():p+=2*(c>_)-1;j=(i,j)[j<k or-p!=x];m=(i,m)[m<k or p!=0];i+=1
 print((j<k)+(j+m<k)*(k+~j)//-~m)