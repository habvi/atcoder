from collections import Counter

def score(S):
    return sum(i * 10**S.count(str(i)) for i in range(1, 10))

def new_score(S, x):
    count_ = S.count(str(x))
    return x * 10**(count_ + 1) - x * 10**count_


K = int(input())
S = input()
T = input()

takahashi = score(S)
aoki = score(T)

c = Counter([*map(int, S[:4]), *map(int, T[:4])])

ans = 0
for t in range(1, 10):
    if c[t] == K:
        continue

    c[t] += 1
    for a in range(1, 10):
        if c[a] == K:
            continue
        nt = takahashi + new_score(S, t)
        na = aoki + new_score(T, a)
        if nt > na:
            ans += (K - c[t] + 1)  * (K - c[a])
    c[t] -= 1

res = K * 9 - 8
print(ans / (res * (res - 1)))