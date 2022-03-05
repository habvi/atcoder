from collections import Counter

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


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ca = Counter(A)
cb = Counter(B)
if ca != cb:
    print('No')
    exit()

if any(v >= 2 for v in ca.values()):
    print('Yes')
    exit()

mx = max(A) + 1
inv_a = inversion_number(A, mx)
inv_b = inversion_number(B, mx)

print('Yes' if inv_a % 2 == inv_b % 2 else 'No')