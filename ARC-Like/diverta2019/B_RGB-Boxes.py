R, G, B, n = map(int, input().split())

ans = 0
for r in range(n // R + 1):
    for g in range(n // G + 1):
        b = n - r * R - g * G
        if b >= 0 and b % B == 0:
            ans += 1
print(ans)