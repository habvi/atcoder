from itertools import groupby

def gen(S):
    a1 = []
    a2 = []
    for k, v in groupby(S):
        lv = len(list(v))
        a1.append((k, lv))
        if lv >= 2:
            lv = 2
        a2.append(lv)
    return a1, a2


S = input()
T = input()

s1, s2 = gen(S)
t1, t2 = gen(T)
for (sk, sl), (tk, tl) in zip(s1, t1):
    if sk !=  tk or sl > tl:
        print('No')
        exit()
print('Yes' if s2 == t2 else 'No')