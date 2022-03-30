n, H = map(int, input().split())

sword = []
for _ in range(n):
    a, b = map(int, input().split())
    sword.append((a, 1))
    sword.append((b, 0))
sword.sort(reverse=True)

ans = 0
for pt, kind in sword:
    if kind:
        ans += (H + pt - 1) // pt
        break

    H -= pt
    ans += 1
    if H <= 0:
        break

print(ans)