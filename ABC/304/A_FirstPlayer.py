N = int(input())
names = []
INF = float('inf')
mn = INF
mn_i = None
for i in range(N):
    s, a = input().split()
    a = int(a)
    names.append(s)
    if a < mn:
        mn = a
        mn_i = i
print(*names[mn_i:], *names[:mn_i])