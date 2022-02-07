from bisect import bisect_left

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
bi = {b : i for i, b in enumerate(B)}

lis = [float('inf')] * (n + 1)
for a in A:
    mlt = []
    for i in range(a, n + 1, a):
        mlt.append(bi[i])
    mlt.sort(reverse=True)

    for m in mlt:
        i = bisect_left(lis, m)
        lis[i] = m

ans = bisect_left(lis, n + 1)
print(ans)