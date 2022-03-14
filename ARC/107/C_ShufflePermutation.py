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


n, K = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(n)]
MOD = 998244353

uf1 = UnionFind(n)
uf2 = UnionFind(n)

for i in range(n):
    for j in range(i + 1, n):
        ok1 = True
        ok2 = True
        for k in range(n):
            if A[i][k] + A[j][k] > K:
                ok1 = False

            if A[k][i] + A[k][j] > K:
                ok2 = False

        if ok1:
            uf1.unite(i, j)
        if ok2:
            uf2.unite(i, j)

m = n**2 + 1
fact = [1] * m
for i in range(1, m):
    fact[i] = fact[i - 1] * i % MOD

ans = 1
for i in range(n):
    if uf1.root(i) == i:
        ans *= fact[uf1.size(i)]

    if uf2.root(i) == i:
        ans *= fact[uf2.size(i)]

    ans %= MOD
print(ans)