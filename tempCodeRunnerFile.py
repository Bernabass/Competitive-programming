output=[]
final=[]
for i in range(len(changed)):
    for j in range(i+1,len(changed)):
        if (changed[i]*2)==changed[j]:
            output.append(changed[i])
            changed[j]='x'
            break
for i in output:
    final.append(i)
    final.append(i*2)
print(final)
if set(final)==set(changed):