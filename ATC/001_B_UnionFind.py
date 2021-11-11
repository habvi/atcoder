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

def q1(a, b):
    UF.unite(a, b)
def q2(a, b):
    return UF.is_same(a, b)

n, q = map(int, input().split())
UF = UnionFind(n)
for i in range(q):
    p, a, b = map(int, input().split())
    if p == 0: q1(a, b)
    else:
        ans = q2(a, b)
        print('Yes' if ans else 'No')