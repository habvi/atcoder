n, m = map(int, input().split())

ans = min(n, m // 2)
m -= ans * 2
ans += m // 4
print(max(0, ans))