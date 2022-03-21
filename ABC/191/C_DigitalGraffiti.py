h, w = map(int, input().split())
S = [input() for _ in range(h)]

ans = 0
for i in range(h - 1):
    for j in range(w - 1):
        sharp = 0
        for y in range(2):
            for x in range(2):
                if S[i + y][j + x] == '#':
                    sharp += 1

        if sharp in (1, 3):
            ans += 1
print(ans)