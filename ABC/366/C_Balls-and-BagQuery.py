from collections import defaultdict

kind = defaultdict(int)

Q = int(input())
for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        x = int(q[1])
        kind[x] += 1
    elif q[0] == "2":
        x = int(q[1])
        kind[x] -= 1
        if not kind[x]:
            del kind[x]
    else:
        print(len(kind))
