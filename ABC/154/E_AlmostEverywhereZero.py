from itertools import combinations

def zero(i, j):
    count_ = 0
    for s in S[i + 1 : j]:
        count_ += (s == '0')
    return count_ == j - i - 1

def left(i):
    zero, one = map(S[:i + 1].count, '01')
    return one + zero == i + 1 and one >= 2


S = input()
K = int(input())
n = len(S)

if n < K:
    print(0)
    exit()

ans = 0
if K == 1:
    ans += int(S[0]) + 9 * (n - 1)
elif K == 2:
    for (i, j) in combinations(range(n), K):
        if i == 0:
            a, b = map(int, (S[i], S[j]))
            if j == 1 or zero(0, j):
                ans += (a - 1) * 9 + b
            else:
                ans += a * 9
        else:
            ans += 9 * 9
else:
    for (i, j, k) in combinations(range(n), K):
        if i == 0:
            a, b, c = map(int, (S[i], S[j], S[k]))
            if a == 1 and b in (0, 1) and not left(j):
                continue
            if j == 1 or zero(i, j):
                ans += (a - 1) * 9 * 9
                ans += max(0, b - 1) * 9
                if k - j == 1 or zero(j, k):
                    ans += c
                else:
                    ans += 9
            else:
                ans += a * 9 * 9
        else:
            ans += 9 ** 3

print(ans)