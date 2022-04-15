from math import pi

n = int(input())
R = sorted(int(input()) for _ in range(n))

ans = 0
for i, r in enumerate(reversed(R)):
    ans += r**2 * (-1 if i % 2 else 1)
print(ans * pi)