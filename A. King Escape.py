def checker():
    n = int(input())
    ai, aj = map(int, input().split())
    bi, bj = map(int, input().split())
    ci, cj = map(int, input().split())
    if(bi < ai and ci > ai):
        return 'NO'
    if(bi > ai and ci < ai):
        return 'NO'
    if(bj < aj and cj > aj):
        return 'NO'
    if(bj > aj and cj< aj):
        return 'NO'
    return 'YES'
print(checker())