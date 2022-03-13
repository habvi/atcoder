import sys
sys.setrecursionlimit(10**7)

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
m = 4 * 10**5

uf = UnionFind(m)
for _ in range(n):
    a, b = map(lambda x: int(x) - 1, input().split())
    uf.unite(a, b)

ans = 0
for i in range(m):
    if uf.root(i) == i:
        ans += min(uf.size(i), uf.edge[i])
print(ans)