from collections import deque
def bfs(seen, xor):
    global ans
    q = deque([])
    q.append((seen, xor))
    while q:
        seen, xor = q.popleft()
        for fst in range(n2):
            if not seen >> fst & 1:
                seen |= 1 << fst
                break
        else:
            ans = max(ans, xor)
            continue
        
        for scd in range(n2):
            if not seen >> scd & 1:
                q.append((seen | 1 << scd, xor ^ A[fst][scd]))
        
n = int(input())
n2 = 2 * n
A = [[-1] * n2 for _ in range(n2)]
for i in range(n2 - 1):
    A[i][i + 1:] = map(int, input().split())

ans = 0
bfs(0, 0)
print(ans)