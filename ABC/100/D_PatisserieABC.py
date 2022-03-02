n, m = map(int, input().split())
xyz = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for pm in range(1 << 3):
    cand = []
    for x in xyz:
        total = 0
        for i in range(3):
            if pm >> i & 1:
                total += -x[i]
            else:
                total += x[i]
        cand.append(total)
    cand.sort(reverse=True)

    ans = max(ans, sum(cand[:m]))
print(ans)