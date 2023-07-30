def check_each_grid(si, sj):
    for i in range(GRID):
        for j in range(GRID):
            if (i <= 2 and j <= 2) and (S[si + i][sj + j] != '#'):
                return False
            if (6 <= i and 6 <= j) and (S[si + i][sj + j] != '#'):
                return False
            if (i == 3 and j <= 3) and (S[si + i][sj + j] == '#'):
                return False
            if (i == 5 and 5 <= j) and (S[si + i][sj + j] == '#'):
                return False
            if (j == 3 and i <= 3) and (S[si + i][sj + j] == '#'):
                return False
            if (j == 5 and 5 <= i) and (S[si + i][sj + j] == '#'):
                return False
    return True


GRID = 9
N, M = map(int, input().split())
S = [input() for _ in range(N)]

for i in range(N - GRID + 1):
    for j in range(M - GRID + 1):
        if check_each_grid(i, j) == True:
            print(i + 1, j + 1)
