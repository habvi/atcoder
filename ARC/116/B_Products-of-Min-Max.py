n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
MOD = 998244353

ans = 0
ac = 0
for a in A:
    ans += a * (a + ac)
    ans %= MOD

    ac = a + ac * 2
    ac %= MOD
print(ans)