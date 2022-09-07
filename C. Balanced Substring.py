n=int(input())
s=input()
count=0
dict={0:0}
out=0
for r in range(n):
    if s[r] == '1':
        count+=1
    else:
        count-=1
    if count in dict:
        out=max(out,r-dict[count]+1)
    else:
        dict[count]=r+1  
print(out)