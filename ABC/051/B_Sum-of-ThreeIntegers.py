K, S = map(int, input().split())

ans = 0
for i in range(K + 1):
    for j in range(K + 1):
        ans += (0 <= S - i - j <= K)

print(ans)