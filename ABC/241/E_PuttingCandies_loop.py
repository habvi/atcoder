from collections import defaultdict

def find_loop(nxt_idx, start, step):
    idx = defaultdict(lambda : -1)
    route = []
    now = start
    num = []
    for i in range(len(nxt_idx)):
        idx[now] = i
        route.append(now)
        num.append(A[now])
        now = nxt_idx[now]
        if now in idx:
            break

    loop = idx[now]
    if step < loop:
        return route[step], sum(num[:step])

    route = route[loop:]
    total = sum(num[:loop])
    num = num[loop:]
    step -= loop
    m = len(num)
    total += step // m * sum(num) + sum(num[:step % m])

    return route[step % len(route)], total


n, K = map(int, input().split())
A = list(map(int, input().split()))

nxt = []
for i, a in enumerate(A):
    nxt.append((i + a) % n)

idx, total = find_loop(nxt, 0, K)
print(total)