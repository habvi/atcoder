N = int(input())
A = [input() for _ in range(N)]

ans = 0
for y in range(N):
    for x in range(N):
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy == dx == 0:
                    continue
                num = []
                ny, nx = y, x
                for _ in range(N):
                    ny = (ny + dy) % N
                    nx = (nx + dx) % N
                    num.append(A[ny][nx])
                ans = max(ans, int(''.join(num)))
print(ans)