from collections import defaultdict

class BIT:
    def __init__(self, len_a):
        self.N = len_a + 10
        self.tree = [0] * (len_a + 10)
    def prod(self, i):
        res = 0
        while i:
            res += self.tree[i]
            i -= i & (-i)
        return res
    def update(self, i, x):
        while i < self.N:
            self.tree[i] += x
            i += i & (-i)


n, Q = map(int, input().split())
C = list(map(int, input().split()))

pre = defaultdict(int)
idx = defaultdict(int)
for i, c in enumerate(C, 1):
    if pre[c]:
        idx[i] = pre[c]
    pre[c] = i

qs = defaultdict(list)
for i in range(Q):
    l, r = map(int, input().split())
    qs[r].append((l, i))

bit = BIT(n)
ans = [None] * Q
for r in range(1, n + 1):
    if idx[r]:
        bit.update(idx[r], 1)

    if qs[r]:
        for l, qi in qs[r]:
            ans[qi] = r - l + 1 - (bit.prod(r) - bit.prod(l - 1))

print(*ans)