n, m = map(int, input().split())

K = []
S = []
for _ in range(m):
    k, *s = map(int, input().split())
    K.append(k)
    S.append(tuple(map(lambda x: x - 1, s)))

P = list(map(int, input().split()))

ans = 0
for bit in range(1 << n):
    light = 0
    for k, ss, p in zip(K, S, P):
        inc = 0
        for s in ss:
            if bit >> s & 1:
               inc += 1

        light += (inc % 2 == p)

    ans += (light == m)
print(ans)