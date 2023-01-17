from collections import defaultdict
t = int(input())

for test_cases in range(t):
    m, n = map(int,input().split())
    board = []
    upper_diagonal, lower_diagonal = defaultdict(int), defaultdict(int)
    maximal_attack = 0
    
    for r in range(m):
        row = list(map(int,input().split()))
        board.append(row)

    for row in range(m):
        for col in range(n):
            upper_diagonal[row-col] += board[row][col]
            lower_diagonal[row+col] += board[row][col]

    for row in range(m):
        for col in range(n):
            curr_square = board[row][col]
            curr_attacks = upper_diagonal[row-col] + lower_diagonal[row+col] - curr_square
            maximal_attack = max(maximal_attack,curr_attacks)

    print(maximal_attack)
