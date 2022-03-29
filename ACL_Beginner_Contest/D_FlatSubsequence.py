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



n, K = map(int, input().split())

m = 3 * 10**5 + 5
seg = SegTree(m, 0)
for _ in range(n):
    a = int(input())

    l = max(0, a - K)
    r = min(m - 1, a + K)
    mx = seg.prod(l, r + 1)
    seg.update(a, mx + 1)

print(seg.prod(0, m))