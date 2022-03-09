from collections import defaultdict

def is_ok(num):
    for a in num:
        for b in num:
            if a == b:
                continue
            if not (a in g[b] and b in g[a]):
                return False
    return True


n, m = map(int, input().split())
g = defaultdict(lambda : set())
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].add(b)
    g[b].add(a)

ans = 0
for bit in range(1 << n):
    num = []
    count_ = 0
    for i in range(n):
        if bit >> i & 1:
            num.append(i)
            count_ += 1

    if is_ok(num):
        ans = max(ans, count_)

print(ans)