from collections import defaultdict
n = int(input())
P = list(map(int, input().split()))
from_ = defaultdict(int)
to_ = defaultdict(int)
for i, p in enumerate(P):
    from_[p] = i
    to_[p] = p - 1

done = [0] * (n - 1)
route = []
fin = 0
for k in range(n, 0, -1):
    while from_[k] != to_[k]:
        left = from_[k]
        right = left + 1
        if done[left]:
            fin = 1
            break
        done[left] = 1
        route.append(left + 1)

        from_[k], from_[P[right]] = from_[P[right]], from_[k]
        P[left], P[right] = P[right], P[left]
    if fin:
        break

def check(P):
    return all([1 if i == p else 0 for i, p in enumerate(P, 1)])

if check(P) and len(route) == n - 1:
    print(*route)
else:
    print(-1)