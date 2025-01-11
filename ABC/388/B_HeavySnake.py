N, D = map(int, input().split())
TL = [tuple(map(int, input().split())) for _ in range(N)]

for extend_length in range(1, D + 1):
    mx = 0
    for t, l in TL:
        mx = max(mx, t * (l + extend_length))
    print(mx)
