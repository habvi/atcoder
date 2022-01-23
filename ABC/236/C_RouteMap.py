n, m = map(int, input().split())
S = input().split()
T = input().split()

st = set(T)
for s in S:
    if s in st:
        print('Yes')
    else:
        print('No')