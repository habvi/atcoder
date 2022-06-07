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

bit = BIT(n)
for _ in range(Q):
    t, k = map(int, input().split())
    if t == 1:
        num = bit.prod(k + (n - k)*2 + 1) if k > n else bit.prod(k)
        if num % 2:
            print(k + (n - k)*2 + 1)
        else:
            print(k)
    else:
        bit.update(n - k + 1, 1)