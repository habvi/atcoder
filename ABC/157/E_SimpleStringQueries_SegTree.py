class SegTree:
    def __init__(self, N, ele):
        self.num = 2**(N - 1).bit_length()
        self.el = ele
        self.data = [ele] * (2*self.num)

    def calc(self, x, y):
        return x | y

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


n = int(input())
S = input()

seg = SegTree(n, 0)
for i, s in enumerate(S):
    x = ord(s) - ord('a')
    seg.update(i, 1 << x)

Q = int(input())
for _ in range(Q):
    q, a, b = input().split()
    a = int(a) - 1

    if q == '1':
        x = ord(b) - ord('a')
        seg.update(a, 1 << x)
    else:
        b = int(b)
        ans = seg.prod(a, b)
        print(bin(ans).count('1'))