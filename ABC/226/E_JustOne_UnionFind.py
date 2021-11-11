import sys
sys.setrecursionlimit(10**7)

class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n
        self.edge = [0]*n
    def root(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]
    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            self.edge[x] += 1
            return False
        if self.parent[x] < self.parent[y]:
            x, y = y, x
        self.size[x] += self.size[y]
        self.parent[y] = x
        self.edge[x] += self.edge[y] + 1
        return True
    def is_same(self, x, y):
        return self.root(x) == self.root(y)
    def set_size(self, x):
        return self.size[self.root(x)]

n, m = map(int, input().split())
MOD = 998244353
UF = UnionFind(n)
for i in range(m):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    UF.unite(u, v)

roots = set()
for i in range(n):
    roots.add(UF.root(i))

for r in roots:
    if UF.edge[r] != UF.set_size(r):
        print(0)
        exit()
print(pow(2, len(roots), MOD))