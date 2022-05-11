from collections import defaultdict
from itertools import accumulate

def find_loop(nxt_idx, start):
    idx = defaultdict(lambda : -1)
    now = start
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
        div, mod = divmod(K, m)
        mx_all = max(ac)
        if not mod:
            total = mx_all
            if tail > 0:
                total = max(total, tail * max(0, div - 1) + mx_all)
        else:
            mx = max(ac[:mod])
            total = mx
            if div:
                total = max(total, mx_all)
            if tail > 0:
                total = max(total,
                            tail * div + max(0, mx),
                            tail * max(0, div - 1) + mx)

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