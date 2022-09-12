from itertools import groupby

def solve():
    gs = [(k, len(list(v))) for k, v in groupby(S)]
    gt = [(k, len(list(v))) for k, v in groupby(T)]
    if len(gs) != len(gt):
        return False

    for (s, sv), (t, tv) in zip(gs, gt):
        if s != t or sv > tv:
            return False
        if sv == 1 and tv != 1:
            return False
    return True


S = input()
T = input()
print("Yes" if solve() else "No")
