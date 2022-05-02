from itertools import accumulate

class SegTree:
    def __init__(self, N, ele):
        self.num = 2**(N - 1).bit_length()
        self.el = ele
        self.data = [ele] * (2*self.num)

    def calc(self, x, y):
        return min(x, y)

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


n, m = map(int, input().split())

imos = [0] * (n + 2)
st = []
for _ in range(m):
    s, t = map(int, input().split())
    imos[s] += 1
    imos[t + 1] -= 1
    st.append((s, t))

INF = float('inf')
seg = SegTree(n + 2, INF)
for i, num in enumerate(accumulate(imos)):
    seg.update(i, num)

ans = []
for i, (s, t) in enumerate(st, 1):
    if seg.prod(s, t + 1) >= 2:
        ans.append(i)

print(len(ans))
for a in ans:
    print(a)