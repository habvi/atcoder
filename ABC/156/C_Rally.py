n = int(input())
X = list(map(int, input().split()))
ans = float('inf')
for p in range(min(X), max(X) + 1):
    tot = 0
    for x in X:
        tot += (x - p)**2
    ans = min(ans, tot)
print(ans)