n = int(input())
a, b = map(int, input().split())
k = int(input())
P = list(map(int, input().split()))

s = set(P)
if len(s) != k or a in s or b in s:
    print('NO')
else:
    print('YES')