from bisect import bisect

def both_side(C):
    i = bisect(C, x)
    if i == 0:
        cand = [C[0]]
    elif i == len(C):
        cand = [C[-1]]
    else:
        cand = [C[i - 1], C[i]]
    return cand


A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]

for _ in range(Q):
    x = int(input())

    cand1 = both_side(S)
    cand2 = both_side(T)

    ans = float('inf')
    for first in cand1:
        for second in cand2:
            if first > second:
                f, s = second, first
            else:
                f, s = first, second

            if s <= x:
                dist = x - f
            elif x <= f:
                dist = s - x
            else:
                mn = min(s - x, x - f)
                mx = max(s - x, x - f)
                dist = mn * 2 + mx

            ans = min(ans, dist)
    print(ans)