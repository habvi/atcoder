from collections import defaultdict
from itertools import accumulate

def find_loop(nxt_idx, now):
    idx = defaultdict(lambda : -1)
    num = []
    for i in range(len(nxt_idx)):
        idx[now] = i
        seen[now] = 1
        num.append(C[now])
        now = nxt_idx[now]
        if now in idx:
            break
    return num

def calc_score(A):
    global ans
    m = len(A)
    for _ in range(m):
        ac = list(accumulate(A))
        tail = ac[-1]

        for i, now in enumerate(ac, 1):
            if i > K:
                break
            loop = (K - i) // m
            if tail < 0:
                loop = 0
            total = tail * loop + now
            ans = max(ans, total)

        A = [*A[1:], A[0]]


n, K = map(int, input().split())
P = list(map(lambda x: int(x) - 1, input().split()))
C = list(map(int, input().split()))

seen = [0] * n
ans = -float('inf')
for i in range(n):
    if not seen[i]:
        seen[i] = 1
        score = find_loop(P, i)
        calc_score(score)
print(ans)