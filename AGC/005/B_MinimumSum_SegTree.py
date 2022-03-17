# https://atcoder.jp/contests/agc005/tasks/agc005_b

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


def dist_to_min(A):
    seg = SegTree(n + 1, 0)
    res = []
    for i, a in enumerate(A, 1):
        mx = seg.prod(0, a)
        res.append(i - mx)
        seg.update(a, i)
    return res


n = int(input())
A = list(map(int, input().split()))

left = dist_to_min(A)
right = dist_to_min(A[::-1])[::-1]

ans = 0
for l, r, a in zip(left, right, A):
    ans += a * l * r
print(ans)