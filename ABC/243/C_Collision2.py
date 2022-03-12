from collections import defaultdict

n = int(input())
xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append((x, y, i))

S = input()

xy.sort(key=lambda x: x[0])

Y = defaultdict(list)
for x, y, i in xy:
    Y[y].append(S[i])

for v in Y.values():
    v = ''.join(v)
    if 'RL' in v:
        print('Yes')
        exit()

print('No')