from collections import defaultdict

def calc_mex(x):
    for i in range(3):
        if not (x & (1 << i)):
            return i
    return 3


N = int(input())
A = list(map(int, input().split()))
S = input()

m = defaultdict(int)
me = defaultdict(int)
mex = defaultdict(int)
total = 0
for s, a in zip(S, A):
    if s == 'M':
        m[1 << a] += 1
    elif s == 'E':
        for k, v in m.items():
            me[k | (1 << a)] += v
    else:
        for k, v in me.items():
            mex[k | (1 << a)] += v
        for k, v in mex.items():
            total += calc_mex(k) * v
    mex = defaultdict(int)
print(total)