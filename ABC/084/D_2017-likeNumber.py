from itertools import accumulate
def furui(x):
    memo = [0]*(x+1)
    primes = []
    for i in range(2, x+1):
        if memo[i]: continue
        primes.append(i)
        memo[i] = i
        for j in range(i*i, x+1, i):
            if memo[j]: continue
            memo[j] = i
    return memo, primes

MAX = 10**5+5
memo, primes = furui(MAX)
simi = [0]*MAX
for i in range(3, MAX-2, 2):
    if memo[i] == i and memo[(i+1)//2] == (i+1)//2:
        simi[i] = 1

ac = list(accumulate(simi))

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(ac[r] - ac[l-1])
