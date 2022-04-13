n = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

K = 60
exp = 1
ans = 0
for i in range(K):
    zero, one = 0, 0
    for a in A:
        if a >> i & 1:
            one += 1
        else:
            zero += 1

    ans += one * zero * exp
    ans %= MOD

    exp *= 2
    exp %= MOD

print(ans)