def to_set(A):
    s = set()
    for i in range(n):
        for j in range(n):
            if A[i][j] == '#':
                s.add((i, j))
    return s

def rotate(A):
    s = set((j, -i) for i, j in A)
    return s


n = int(input())
S = [input() for _ in range(n)]
T = [input() for _ in range(n)]

ss = to_set(S)
st = to_set(T)

for _ in range(4):
    mi, mj = min(ss)
    shape1 = set((i - mi, j - mj) for i, j in ss)

    mi, mj = min(st)
    shape2 = set((i - mi, j - mj) for i, j in st)

    if shape1 == shape2:
        print('Yes')
        exit()

    st = rotate(st)
print('No')