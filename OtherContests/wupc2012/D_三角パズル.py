n = int(input())

dp = [int(input())]
for i in range(n - 1):
    nxt = tuple(map(int, input().split()))
    ndp = [0] * (i + 2)
    for j, num in enumerate(dp):
        ndp[j] = max(ndp[j], nxt[j] + num)
        ndp[j + 1] = max(ndp[j + 1], nxt[j + 1] + num)
    dp = ndp

print(max(dp))