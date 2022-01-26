from itertools import accumulate

n, q = map(int, input().split())
S = input()

cnt = [0] * n
for i in range(1, n):
    if S[i - 1 : i + 1] == 'AC':
        cnt[i] += 1

ac = list(accumulate(cnt))
for _ in range(q):
    l, r = map(int, input().split())
    print(ac[r - 1] - ac[l - 1])