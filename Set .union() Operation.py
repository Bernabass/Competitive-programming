# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
english = input().split()
n3 = int(input())
french = input().split()
res = len((set(english).union(set(french))))
print(res)