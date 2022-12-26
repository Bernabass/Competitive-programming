if __name__ == '__main__':
    N = int(input())
    List = []
    for i in range(N):
        inp = input().split()

        if inp[0] == "insert":
            List.insert(int(inp[1]),int(inp[2]))
        elif inp[0] == "print":
            print(List)
        elif inp[0] == "remove":
            List.remove(int(inp[1]))
        elif inp[0] == "append":
            List.append(int(inp[1]))
        elif inp[0] == "sort":
            List.sort()
        elif inp[0] == "pop":
            List.pop()
        else:
            List.reverse()