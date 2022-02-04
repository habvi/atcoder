A = [int(input()) for _ in range(5)]

mn = 10
for a in A:
    if a % 10:
        mn = min(mn, a % 10)

ans = 0
for a in A:
    ans += (a + 9) // 10 * 10
print(ans - 10 + mn)