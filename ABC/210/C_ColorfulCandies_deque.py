from collections import defaultdict, deque

n, k = map(int, input().split())
C = list(map(int, input().split()))

kind = defaultdict(int)
q = deque([])
ans = 0
for c in C:
    q.append(c)
    kind[c] += 1

    while q and len(q) > k:
        rm = q.popleft()
        kind[rm] -= 1
        if not kind[rm]:
            del kind[rm]

    ans = max(ans, len(kind))

print(ans)