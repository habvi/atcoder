N, M = map(int, input().split())
ka = [tuple(map(int, input().split())) for _ in range(N)]
P, Q = map(int, input().split())
B = set(map(int, input().split()))

ans = 0
for k, *A in ka:
    tmp = 0
    for a in A:
        tmp += (a in B)
    ans += (tmp >= Q)
print(ans)