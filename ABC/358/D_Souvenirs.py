N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = 0
bi = 0
for a in A:
    if bi >= M:
        break
    if a >= B[bi]:
        ans += a
        bi += 1
print(ans if bi == M else -1)
