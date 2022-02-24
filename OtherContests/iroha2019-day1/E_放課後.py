n, a, b = map(int, input().split())
D = [0, *map(int, input().split()), n + 1]
D.sort()

ans = 0
for i in range(len(D) - 1):
    if (day := D[i + 1] - D[i] - 1) >= a:
        ans += day - day // a
    else:
        ans += day

print(ans)  