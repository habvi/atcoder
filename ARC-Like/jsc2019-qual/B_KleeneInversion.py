from bisect import bisect

class FenwickTree:
    def __init__(self, n=0, *, array=None):
        assert (n > 0 and array is None) or (n == 0 and array)

        if array:
            n = len(array)
            self.__array = array[:]  # get用
            _container = array[:]
            for i in range(n):
                j = i | (i + 1)
                if j < n:
                    _container[j] += _container[i]
            self.__size = len(array) + 1
            self.__container = [0] + _container[:]
            self.__depth = n.bit_length()
        else:
            self.__array = [0] * n
            self.__size = n + 1
            self.__container = [0] * (n + 1)
            self.__depth = n.bit_length()

    def add(self, i, x):
        """a[i]にxを加算"""
        self.__array[i] += x
        i += 1
        while i < self.__size:
            self.__container[i] += x
            i += i & (-i)

    def sum(self, r):
        """[0, r) の総和"""
        s = 0
        while r > 0:
            s += self.__container[r]
            r -= r & (-r)
        return s

    def sum_range(self, l, r):
        """[l, r) の総和"""
        return self.sum(r) - self.sum(l)

    def upper_bound(self, s):
        """[0, r) の総和 <= s となる最大のrを求める"""
        w, r = 0, 0
        for i in reversed(range(self.__depth)):
            k = r + (1 << i)
            if k < self.__size and w + self.__container[k] <= s:
                w += self.__container[k]
                r += 1 << i
        return r

    def set(self, i, x):
        """a[i]をxに変更"""
        self.add(i, x - self.__array[i])

    def get(self, i):
        """a[i]を返す"""
        return self.__array[i]

    def __getitem__(self, key):
        if isinstance(key, slice):
            start, stop = key.start, key.stop
            if start is None: start = 0
            if stop is None: stop = self.__size - 1
            if start == 0: return self.sum(stop)
            return self.sum_range(start, stop)
        else:
            return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)

def inversion_number(A, n):
    bit = FenwickTree(n)
    count_ = 0
    for a in A:
        count_ += bit.sum_range(a + 1, n)
        bit.add(a, 1)
    return count_

def sigma_adn(a, d, n):
    return (2*a + (n - 1)*d) * n // 2


n, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9 + 7

mx = max(A) + 1
inv = inversion_number(A, mx) % MOD

A.sort()
larger = 0
for a in A:
    bi = bisect(A, a)
    num = n - bi
    larger += sigma_adn(num, num, K - 1)

ans = inv * K + larger
print(ans % MOD)