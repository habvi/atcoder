# https://atcoder.jp/contests/abc103/tasks/abc103_d

n, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(m)]

ab.sort(key=lambda x: x[1])

back = -1
ans = 0
for a, b in ab:
    if a < back:
        continue
    ans += 1
    back = b

print(ans)