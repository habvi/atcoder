n = int(input())
S = input()

lb = [0] * n
rw = [0] * n

black = 0
white = 0
for i in range(n):
    black += (S[i] == '#')
    lb[i] = black

    white += (S[~i] == '.')
    rw[~i] = white

lb = [0, *lb]
rw.append(0)

ans = float('inf')
for i in range(n + 1):
    ans = min(ans, lb[i] + rw[i])

print(ans)