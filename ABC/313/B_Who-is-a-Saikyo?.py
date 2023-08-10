N, M = map(int, input().split())

out_deg = set(range(1, N + 1))
for _ in range(M):
    a, b = map(int, input().split())
    out_deg.discard(b)
print(out_deg.pop() if len(out_deg) == 1 else -1)