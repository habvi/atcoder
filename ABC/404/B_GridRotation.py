def r_rotate(G):
    return ["".join(reversed(g)) for g in zip(*G)]

def calc(S, T):
    convert = 0
    for i in range(N):
        for j in range(N):
            if S[i][j] != T[i][j]:
                convert += 1
    return convert

N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

INF = float('inf')
ans = INF
for rotate_count in range(4):
    ans = min(ans, calc(S, T) + rotate_count)
    S = r_rotate(S)
print(ans)
