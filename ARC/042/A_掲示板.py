n, m = map(int, input().split())
s = [i for i in range(n)]

mn = 0
for _ in range(m):
    a = int(input())
    a -= 1
    s[a] = mn - 1
    mn = s[a]

lis = sorted([(v, i) for i, v in enumerate(s)])
for v, ans in lis:
    print(ans + 1)