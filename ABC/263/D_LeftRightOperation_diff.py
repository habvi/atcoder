# 解説放送

N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans = R * N
# ac_b = Σ(a[i] - L)
ac_a, ac_b = 0, 0
mx = 0
for i, a in enumerate(A):
    ac_a += a
    ac_b += (a - L)
    mx = max(mx, ac_b)
    now = ac_a + R * (N - i - 1) - mx
    ans = min(ans, now)
print(ans)