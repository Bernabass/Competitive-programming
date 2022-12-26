# The code only works in Pypy 3 and I have no idea why it's not working on python 3
if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))
    print(hash(t))