from collections import defaultdict

N, Q = map(int, input().split())

yellow = defaultdict(int)
red = defaultdict(int)
for _ in range(Q):
    q, x = map(int, input().split())
    if q == 1:
        yellow[x] += 1
    elif q == 2:
        red[x] += 1
    else:
        if yellow[x] == 2 or red[x] == 1:
            print("Yes")
        else:
            print("No")