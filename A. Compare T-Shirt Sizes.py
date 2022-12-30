t = int(input())
for _ in range(t):
    shirts = input().split()
    shirtA = shirts[0]
    shirtB = shirts[1]
    info = {"S":0,"M":1,"L":2}
    if info[shirtA[-1]] == info[shirtB[-1]]:
        if shirtA[-1] == "S":
            if len(shirtA) < len(shirtB):
                print(">")
            elif len(shirtA) > len(shirtB):
                print("<")
            else:
                print("=")
        else:
            if len(shirtA) < len(shirtB):
                print("<")
            elif len(shirtA) > len(shirtB):
                print(">")
            else:
                print("=")
    elif info[shirtA[-1]] > info[shirtB[-1]]:
        print(">")
    else:
        print("<")