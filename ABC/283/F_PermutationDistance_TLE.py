class SegTreeMin:
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

class SegTreeMax:
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


N = int(input())
P = list(map(int, input().split()))
pi = [(p, i) for i, p in enumerate(P)]

INF = 10 ** 10
ans = [INF] * N
s = SegTreeMin(N, INF)
for p, i in sorted(pi, reverse=True):
    mn = s.prod(i, N)
    if mn != INF:
        ans[i] = min(ans[i], mn - p - i)
    s.update(i, p + i)

s = SegTreeMin(N, INF)
for p, i in sorted(pi, reverse=True):
    mn = s.prod(0, i)
    if mn != INF:
        ans[i] = min(ans[i], mn - p + i)
    s.update(i, p - i)

s = SegTreeMax(N, -INF)
for p, i in sorted(pi):
    mx = s.prod(i, N)
    if mx != -INF:
        ans[i] = min(ans[i], p - i - mx)
    s.update(i, p - i)

s = SegTreeMax(N, -INF)
for p, i in sorted(pi):
    mx = s.prod(0, i)
    if mx != -INF:
        ans[i] = min(ans[i], p + i - mx)
    s.update(i, p + i)
print(*ans)
