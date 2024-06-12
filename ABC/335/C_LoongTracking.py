N, Q = map(int, input().split())

d = []
for i in range(N):
    d.append([i + 1, 0])
d = d[::-1]

for i in range(Q):
    x, y = input().split()
    if x == "1":
        C = y
        head = d[-1].copy()
        if C == "L":
            head[0] -= 1
        elif C == "R":
            head[0] += 1
        elif C == "D":
            head[1] -= 1
        else:
            head[1] += 1
        d.append(head)
    else:
        p = int(y)
        print(*d[-p])
