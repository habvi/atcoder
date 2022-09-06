def ul_and_lr(U, h):
    li = -1
    for i in range(h):
        if '#' in U[i]:
            if li == -1:
                li = i
            ri = i
    lj = -1
    for i, u in enumerate(zip(*U)):
        if '#' in u:
            if lj == -1:
                lj = i
            rj = i
    return li, lj, ri, rj

def trm(U, h, w, li, lj):
    res = []
    for i in range(h):
        res.append(U[i + li][lj:lj + w])
    return res

def r_rotate(G):
    return ["".join(reversed(g)) for g in zip(*G)]


N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

li, lj, ri, rj = ul_and_lr(S, N)
h = ri - li + 1
w = rj - lj + 1
part_s = trm(S, h, w, li, lj)

li, lj, ri, rj = ul_and_lr(T, N)
h = ri - li + 1
w = rj - lj + 1
part_t = trm(T, h, w, li, lj)

for _ in range(4):
    if part_s == part_t:
        print("Yes")
        exit()
    part_s = r_rotate(part_s)
print("No")