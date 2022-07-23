def check():
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                a = A[i][j] + A[j][i]
                if not (a == "WL" or a == "LW" or a == "DD"):
                    return False
    return True


n = int(input())
A = [input() for _ in range(n)]

print('correct' if check() else 'incorrect')