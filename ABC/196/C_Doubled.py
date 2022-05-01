n = int(input())

ans = 0
for i in range(1, int(str(n)[:6]) + 1):
    ans += (int(str(i) * 2) <= n)
print(ans)