n = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

K = 60
one = [0] * K
zero = [0] * K
for a in A:
    for i in range(K):
        if a >> i & 1:
            one[i] += 1
        else:
            zero[i] += 1

ans = 0
exp = 1
for i in range(K):
    ans += one[i] * zero[i] * exp
    ans %= MOD

    exp *= 2
    exp %= MOD

print(ans)