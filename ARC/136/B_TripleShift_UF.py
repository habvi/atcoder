from collections import Counter
import sys
sys.setrecursionlimit(10 ** 7)

class UnionFind():
    def __init__(self, n):
        self.rank = [-1] * n
        self.edge = [0] * n
        self.unite_cnt = 0
    def root(self, x):
        if self.rank[x] < 0:
            return x
        self.rank[x] = self.root(self.rank[x])
        return self.rank[x]
    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            self.edge[x] += 1
            return False
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        self.rank[x] += self.rank[y]
        self.rank[y] = x
        self.edge[x] += self.edge[y] + 1
        self.unite_cnt += 1
        return True
    def is_same(self, x, y):
        return self.root(x) == self.root(y)
    def size(self, x):
        return -self.rank[self.root(x)]


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ca = Counter(A)
cb = Counter(B)
if ca != cb:
    print('No')
    exit()

if any(v >= 2 for v in ca.values()):
    print('Yes')
    exit()


def cycle_num(A):
    uf = UnionFind(mx)
    for i, a in enumerate(A):
        uf.unite(a, comp[i])

    count_ = 0
    for i in range(mx):
        if uf.root(i) == i:
            count_ += 1
    return count_


mx = max(A) + 1
comp = dict(enumerate(sorted(A)))

cycle_a = cycle_num(A)
cycle_b = cycle_num(B)

print('Yes' if cycle_a % 2 == cycle_b % 2 else 'No')