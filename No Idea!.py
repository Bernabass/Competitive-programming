# Enter your code here. Read input from STDIN. Print output to STDOUT
n , m = input().split()
array = input().split()
A = set(input().split())
B = set(input().split())
happiness = 0
for i in array:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
print(happiness)