def itoc(i):
    return chr(i + ord('A'))

H, W = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(H)]

for i in range(H):
    s = ""
    for j in range(W):
        c = A[i][j]
        if c:
            s += itoc(c - 1)
        else:
            s += '.'
    print(s)