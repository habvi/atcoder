n = int(input())
P = list(map(int, input().split()))

ans = 0
for i in range(n - 1):
    if P[i] == i + 1:
        P[i], P[i + 1] = P[i + 1], P[i]
        ans += 1

if P[-1] == n:
    ans += 1

print(ans)