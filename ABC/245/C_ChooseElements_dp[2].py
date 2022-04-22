n, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [1, 1]
for i in range(1, n):
    pa, a = A[i - 1], A[i]
    pb, b = B[i - 1], B[i]

    ndp = [0, 0]
    if dp[0]:
        ndp[0] |= (abs(pa - a) <= K)
        ndp[1] |= (abs(pa - b) <= K)
    if dp[1]:
        ndp[0] |= (abs(pb - a) <= K)
        ndp[1] |= (abs(pb - b) <= K)
    dp = ndp

    if not sum(ndp):
        print('No')
        exit()
print('Yes')