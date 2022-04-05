from collections import Counter

n = int(input())
D = list(map(int, input().split()))
MOD = 998244353

c = Counter(D)

if D[0] != 0 or c[0] != 1:
    print(0)
    exit()

ans = 1
for d in D[1:]:
    pre = c[d - 1]
    if not pre:
        print(0)
        exit()

    ans *= pre
    ans %= MOD

print(ans)