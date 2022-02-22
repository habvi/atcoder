# https://atcoder.jp/contests/abc163/tasks/abc163_d

def sigma_aln(a, l, n):
    return n*(a + l) // 2


n, k = map(int, input().split())
MOD = 10**9 + 7

ans = 0
for i in range(k, n + 2):
    mini = sigma_aln(0, i - 1, i)
    maxi = sigma_aln(n + 1 - i, n, i)

    ans += maxi - mini + 1
    ans %= MOD

print(ans)