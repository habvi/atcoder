X = input()
n = len(X)
a = set()
en = 0
for d in range(-8, 9):
    for f in range(1, 10):
        for i in range(1, 18):
            t = [str(f)]
            for _ in range(i):
                nxt = int(t[-1]) + d
                if 0 <= nxt <= 9:
                    t.append(str(nxt))
                else:
                    en = 1
                    break
            a.add(int("".join(t)))
            if en:
                en = 0
                break
a = list(a)
a.sort()

from bisect import bisect_left
bi = bisect_left(a, int(X))
print(a[bi])