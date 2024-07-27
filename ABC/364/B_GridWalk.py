H, W = map(int, input().split())
i, j = map(lambda x: int(x) - 1, input().split())
C = [input() for _ in range(H)]
X = input()

for x in X:
    if x == "U" and i - 1 >= 0 and C[i - 1][j] == ".":
        i -= 1
    elif x == "D" and i + 1 < H and C[i + 1][j] == ".":
        i += 1
    elif x == "L" and j - 1 >= 0 and C[i][j - 1] == ".":
        j -= 1
    elif x == "R" and j + 1 < W and C[i][j + 1] == ".":
        j += 1
print(i + 1, j + 1)
