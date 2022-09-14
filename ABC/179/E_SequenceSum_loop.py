from collections import defaultdict

def find_loop(now, step):
    idx = defaultdict(lambda : -1)
    num = []
    for i in range(M):
        idx[now] = i
        num.append(now)
        now = now * now % M
        if now in idx:
            break

    loop = idx[now]
    if step < loop:
        return sum(num[:step])

    total = sum(num[:loop])
    num = num[loop:]
    step -= loop
    m = len(num)
    total += step // m * sum(num) + sum(num[:step % m])
    return total


N, X, M = map(int, input().split())

total = find_loop(X, N)
print(total)
