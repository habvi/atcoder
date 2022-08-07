def solve(A):
    if len(A) == N:
        print(*A)
        return
    for i in range(A[-1] + 1, M + 1):
        solve(A + [i])


N, M = map(int, input().split())

for i in range(1, M + 1):
    solve([i])