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

pre = defaultdict(lambda : -1)
cs = defaultdict(int)
for i, c in enumerate(C):
    if pre[c] != -1:
        cs[pre[c]] = i
    pre[c] = i

qs = defaultdict(list)
for i in range(Q):
    l, r = map(lambda x: int(x) - 1, input().split())
    qs[l].append((r, i))

bit = BIT(n)
ans = [None] * Q
for l in reversed(range(n)):
    if cs[l]:
        r = cs[l]
        bit.update(r, 1)

    if qs[l]:
        for r, qi in qs[l]:
            ans[qi] = r - l + 1 - bit.prod(r)

print(*ans)