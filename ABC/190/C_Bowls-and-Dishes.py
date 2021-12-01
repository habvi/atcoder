n, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(m)]
K = int(input())
cd = [tuple(map(int, input().split())) for _ in range(K)]
ans = 0
for i in range(1 << K):
    put = [0] * n
    for j in range(K):
        if i & (1<<j):
            put[cd[j][0] - 1] = 1
        else:
            put[cd[j][1] - 1] = 1

    cnt = 0
    for a, b in ab:
        if put[a - 1] and put[b - 1]:
            cnt += 1
    ans = max(ans, cnt)
print(ans)