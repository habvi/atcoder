from collections import defaultdict

n, m, q = map(int, input().split())

score = defaultdict(lambda : n)
solved = defaultdict(list)

for _ in range(q):
    *q, = map(int, input().split())

    if q[0] == 1:
        pi = q[1]
        ans = 0
        for qi in solved[pi]:
            ans += score[qi]
        print(ans)
    else:
        pi, qi = q[1:]
        score[qi] -= 1
        solved[pi].append(qi)