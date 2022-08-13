import sys
sys.setrecursionlimit(10 ** 7)

class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.city_size = [1] * N
        self.city_size.extend([0] * M)
        self.is_light = [0] * N
        self.is_light.extend([1] * M)
    def root(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]
    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return False
        if self.parent[x] < self.parent[y]:
            x, y = y, x
        self.city_size[x] += self.city_size[y]
        self.is_light[y] |= self.is_light[x]
        self.is_light[x] |= self.is_light[y]
        self.parent[y] = x
        return True
    def is_same(self, x, y):
        return self.root(x) == self.root(y)
    def set_city_size(self, x):
        return self.city_size[self.root(x)]



N, M, E = map(int, input().split())
ab = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(E)]

Q = int(input())
X = [int(input()) - 1 for _ in range(Q)]
done = set(X)

total = N + M
uf = UnionFind(total)
for e in range(E):
    if e not in done:
        a, b = ab[e]
        uf.unite(a, b)

for i in range(N):
    uf.root(i)
city_num = 0
for i in set(uf.parent):
    if uf.is_light[i]:
        city_num += uf.set_city_size(i)
ans = [city_num]

for x in X[::-1]:
    a, b = ab[x]
    ra, rb = uf.root(a), uf.root(b)
    if ra == rb:
        ans.append(ans[-1])
        continue

    tmp = ans[-1]
    if uf.is_light[ra]:
        tmp -= uf.set_city_size(ra)
    if uf.is_light[rb]:
        tmp -= uf.set_city_size(rb)
    uf.unite(a, b)
    ra = uf.root(a)
    if uf.is_light[ra]:
        tmp += uf.set_city_size(ra)
    ans.append(tmp)

print(*ans[:-1][::-1])