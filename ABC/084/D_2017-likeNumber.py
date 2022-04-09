from itertools import accumulate

def Sieve(x):
    memo = [0] * (x + 1)
    for i in range(2, x + 1):
        if memo[i]:
            continue
        memo[i] = i
        for j in range(i * i, x + 1, i):
            if memo[j]:
                continue
            memo[j] = i
    return memo


mx = 10 ** 5 + 1
memo = Sieve(mx)

num = [0] * mx
for i in range(1, mx, 2):
    x = (i + 1) // 2
    if memo[i] == i and memo[x] == x:
        num[i] = 1

ac = list(accumulate(num))

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(ac[r] - ac[l - 1])