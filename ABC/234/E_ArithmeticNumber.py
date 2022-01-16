x = input()
n = len(x)
lis = []
fin = False
for fst in range(1, 10):
    lis.append(fst)
    for diff in range(-9, 9):
        t = fst
        while not fin and len(str(t)) <= n:
            if 0 <= t % 10 + diff <= 9:
                t = t * 10 + t % 10 + diff
                lis.append(t)
            else:
                fin = True
        fin = False
lis.sort()

from bisect import bisect_left
bi = bisect_left(lis, int(x))
print(lis[bi])