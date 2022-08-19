N, K = map(int, input().split())

ab = [tuple(map(int, input().split())) for _ in range(N)]
ab.sort(reverse=True)

total = 0
while True:
    a, b = ab.pop()
    total += b
    if total >= K:
        print(a)
        exit()
