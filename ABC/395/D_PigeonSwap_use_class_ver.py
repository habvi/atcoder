class Virtual:
    def __init__(self, x):
        self.nest_num = x


N, Q = map(int, input().split())

nest = [Virtual(i) for i in range(N)]
pigeon = [nest[i] for i in range(N)]
for _ in range(Q):
    q, *op = map(int, input().split())
    if q == 1:
        a, b = op
        a, b = a - 1, b - 1
        pigeon[a] = nest[b]
    elif q == 2:
        a, b = op
        a, b = a - 1, b - 1
        nest[a], nest[b] = nest[b], nest[a]
        nest[a].nest_num, nest[b].nest_num = nest[b].nest_num, nest[a].nest_num
    else:
        a = op[0] - 1
        print(pigeon[a].nest_num + 1)
