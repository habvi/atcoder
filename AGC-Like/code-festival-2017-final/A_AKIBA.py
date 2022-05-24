from itertools import product

S = input()

akiba = ["", "KIH", "", "B", "", "R", ""]
n = 7

cand = set()
for pr in product((0, 1), repeat=4):
    T = akiba[:]
    for i, p in zip(range(0, n, 2), pr):
        if p:
            T[i] = "A"
    cand.add(''.join(T))

print('YES' if S in cand else 'NO')