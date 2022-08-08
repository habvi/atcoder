class BIT:
    def __init__(self, len_a):
        self.N = len_a + 10
        self.tree = [0]*(len_a + 10)
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

def inversion_number(A, n):
    bit = BIT(n)
    count_ = 0
    for a in A:
        count_ += bit.prod(n) - bit.prod(a)
        bit.update(a, 1)
    return count_


from collections import defaultdict

N = int(input())
C = list(map(int, input().split()))
X = list(map(int, input().split()))

ans = inversion_number(X, max(X) + 1)
color = defaultdict(list)
for c, x in zip(C, X):
    color[c].append(x)

for v in color.values():
    cmp = {num : i for i, num in enumerate(sorted(set(v)), 1)}
    new = [cmp[x] for x in v]
    ans -= inversion_number(new, len(cmp) + 1)
print(ans)