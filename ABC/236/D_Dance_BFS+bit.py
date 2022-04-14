from collections import deque

def bfs(seen, xor):
    global ans
    q = deque([])
    q.append((seen, xor))
    while q:
        seen, xor = q.popleft()
        for first in range(n2):
            if not seen >> first & 1:
                seen |= 1 << first
                break
        else:
            ans = max(ans, xor)
            continue

        for second in range(n2):
            if not seen >> second & 1:
                q.append((seen | 1 << second, xor ^ A[first][second]))


n = int(input())
n2 = 2 * n

A = [[-1] * n2 for _ in range(n2)]
for i in range(n2 - 1):
    A[i][i + 1:] = map(int, input().split())

ans = 0
bfs(0, 0)
print(ans)