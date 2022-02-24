n, K = map(int, input().split())
R = list(map(int, input().split()))
R.sort()
R = R[-K:]

ans = 0
for r in R:
    ans = (ans + r) / 2
print(ans)