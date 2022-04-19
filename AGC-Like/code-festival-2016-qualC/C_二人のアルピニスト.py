n = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
MOD = 10**9 + 7

decided = [0] * n
pre = -1
for i, t in enumerate(T):
    if pre < t:
        decided[i] = 1
    pre = t

left = False
pre = -1
ans = 1
for i, a in enumerate(A[::-1]):
    ri = n - i - 1
    if pre < a:
        if decided[ri] and a < T[ri]:
            print(0)
            exit()
    else:
        if decided[ri]:
            left = True
            if a < T[ri]:
                print(0)
                exit()
            pre = a
            continue

        ans *= (T[ri] if left else a)
        ans %= MOD
    pre = a
print(ans)