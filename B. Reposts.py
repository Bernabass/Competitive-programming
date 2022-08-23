n=int(input())
col=[]
dic={}
root = "polycarp"
dic["polycarp"] = 1 
for i in range(n):
  s=list(input().split())
  for j in range(len(s)):
    s[j]=s[j].lower()
  dic[s[0]] = dic[s[2]]+1
maxx=-1
for k in dic.values():
    if k>maxx:
        maxx=k
print(maxx)