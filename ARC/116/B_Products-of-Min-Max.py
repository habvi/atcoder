n = int(input())
A = list(map(int, input().split()))
A.sort()
MOD = 998244353

ans = 0
ac = 0
for a in A:
    ans += a * a
    ans += a * ac
    ans %= MOD
    
    ac = ac * 2 + a
    ac %= MOD
print(ans)