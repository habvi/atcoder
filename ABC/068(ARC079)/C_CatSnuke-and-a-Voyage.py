from collections import defaultdict

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

for v in g[0]:
    for nv in g[v]:
        if nv == n - 1:
            print('POSSIBLE')
            exit()
print('IMPOSSIBLE')



# n, m = map(int, input().split())
# c = []
# for i in range(m):
#     a, b = map(int, input().split())
#     if a == 1:
#         c.append(b)
#     if b == n:
#         c.append(a)

# if len(c) == len(set(c)):
#     print('IMPOSSIBLE')
# else:
#     print('POSSIBLE')