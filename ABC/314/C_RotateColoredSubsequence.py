from collections import defaultdict, deque

N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

color = defaultdict(deque)
for i, c in enumerate(C):
    color[c].append(i)

for v in color.values():
    v.appendleft(v.pop())

for c in C:
    i = color[c].popleft()
    print(S[i], end="")
print()

