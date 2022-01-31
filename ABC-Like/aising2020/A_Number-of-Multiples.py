l, r, d = map(int, input().split())

ans = 0
for i in range(l, r + 1):
    ans += i % d == 0
print(ans)