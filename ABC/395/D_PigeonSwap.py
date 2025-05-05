N, Q = map(int, input().split())

pigeon_to_virtual = [i for i in range(N)]
virtual_to_nest = [i for i in range(N)]
nest_to_virtual = [i for i in range(N)]
for _ in range(Q):
    q, *op = map(int, input().split())
    if q == 1:
        a, b = op
        a, b = a - 1, b - 1
        pigeon_to_virtual[a] = nest_to_virtual[b]
    elif q == 2:
        a, b = op
        a, b = a - 1, b - 1
        nest_to_virtual[a], nest_to_virtual[b] = nest_to_virtual[b], nest_to_virtual[a]
        va, vb = nest_to_virtual[a], nest_to_virtual[b]
        virtual_to_nest[va], virtual_to_nest[vb] = a, b
    else:
        a = op[0] - 1
        print(virtual_to_nest[pigeon_to_virtual[a]] + 1)
