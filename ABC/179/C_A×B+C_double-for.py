N = int(input())

ans = 0
for a in range(1, N + 1):
    for b in range(1, N // a + 1):
        c = N - a * b
        ans += (c >= 1)
print(ans)