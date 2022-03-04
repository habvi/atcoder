a, b, k = map(int, input().split())

l = set(range(a, min(b + 1, a + k)))
r = set(range(b, max(a - 1, b - k), -1))

print(*sorted(l | r))