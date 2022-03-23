from collections import defaultdict

def find_loop(A, start, step):
    idx = defaultdict(lambda : -1)
    route = []
    now = start
    for i in range(len(A)):
        idx[now] = i
        route.append(now)
        now = A[now]
        if now in idx:
            break

    loop = idx[now]
    if step < loop:
        return route[step]

    route = route[loop:]
    step -= loop
    return route[step % len(route)]


n, A = map(int, input().split())
K = int(input())
B = list(map(lambda x: int(x) - 1, input().split()))

A -= 1
ans = find_loop(B, A, K)
print(ans + 1)