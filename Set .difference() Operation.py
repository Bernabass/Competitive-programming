# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
english = input()
n2 = int(input())
french = input()
res = set(english.split()) - set(french.split())
print(len(res))