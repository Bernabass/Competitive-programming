# Enter your code here. Read input from STDIN. Print output to STDOUT
setA = set(input().split())
n = int(input())
for i in range(n):
    setB = set(input().split())
    if not (setB - setA):
        if (setA - setB):
            continue
        else:
            print("False")
            exit()
    else:
        print("False")
        exit()
print("True")