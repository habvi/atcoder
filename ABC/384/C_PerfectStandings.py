ALPH = "ABCDE"

score = tuple(map(int, input().split()))

cand = []
for i in range(1, 1 << 5):
    total = 0
    s = ""
    for j in range(5):
        if (i >> j) & 1:
            total += score[j]
            s += ALPH[j]
    cand.append((s, total))

cand.sort(key=lambda x: (-x[1], x[0]))
for s, _ in cand:
    print(s)
