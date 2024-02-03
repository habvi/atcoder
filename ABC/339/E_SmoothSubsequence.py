class SegTree:
    def __init__(self, N, ele):
        self.num = 2**(N - 1).bit_length()
        self.el = ele
        self.data = [ele] * (2*self.num)

    def calc(self, x, y):
        return max(x, y)

    def update(self, idx, x):
        idx += (self.num - 1)
        self.data[idx] = x
        while idx > 0:
            idx = (idx - 1)//2
            self.data[idx] = self.calc(self.data[2*idx + 1], self.data[2*idx + 2])

    def prod(self, l, r):
        L = l + self.num
        R = r + self.num
        res = self.el
        while L < R:
            if L & 1:
                res  = self.calc(res, self.data[L - 1])
                L += 1
            if R & 1:
                R -= 1
                res = self.calc(res, self.data[R - 1])
            L >>= 1
            R >>= 1
        return res

    def get(self, idx):
        idx += (self.num - 1)
        return self.data[idx]


N, D = map(int, input().split())
A = list(map(int, input().split()))

mx = max(A)
seg = SegTree(mx + 1, 0)
for a in A:
    l = max(0, a - D)
    r = min(mx, a + D)
    pre = seg.prod(l, r + 1)
    seg.update(a, pre + 1)

print(seg.prod(0, mx + 1))