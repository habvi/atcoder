K, S = map(int, input().split())

ans = 0
for x in range(K + 1):
    for y in range(K + 1):
        z = S - x - y
        ans += (0 <= z <= K)
print(ans)