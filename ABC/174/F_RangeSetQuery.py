class BIT:
    def __init__(self, len_a):
        self.N = len_a + 10
        self.tree = [0]*(len_a+10)
    def prod(self, i):
        res = 0
        while i:
            res += self.tree[i]
            i -= i&(-i)
        return res
    def update(self, i, x):
        while i < self.N:
            self.tree[i] += x
            i += i&(-i)
    def lower_left(self, w):
        if w < 0: return -1
        x = 0
        k = 1<<(self.N.bit_length()-1)
        while k > 0:
            if x+k < self.N and self.tree[x+k] < w:
                w -= self.tree[x+k]
                x += k
            k //= 2
        return x


from collections import defaultdict

n, q = map(int, input().split())
C = list(map(int, input().split()))

P = defaultdict(int)
idx = defaultdict(lambda : -1)
for i, c in enumerate(C):
    if idx[c] != -1:
        P[idx[c]] = i
    idx[c] = i

Q = defaultdict(list)
for i in range(q):
    l, r = map(lambda x: int(x) - 1, input().split())
    Q[l].append((r, i))

bit = BIT(n)
ans = [0] * q
for x in range(n - 1, -1, -1):
    if x in P:
        y = P[x]
        bit.update(y, 1)

    for r, i in Q[x]:
        ans[i] = r - x + 1 - bit.prod(r)
print(*ans)