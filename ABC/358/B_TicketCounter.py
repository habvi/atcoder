N, A = map(int, input().split())
T = list(map(int, input().split()))

total = 0
for t in T:
    mn = total + A
    mx = t + A
    total = max(mn, mx)
    print(total)
