C = [tuple(map(int, input().split())) for _ in range(3)]

for i in range(2):
    s = set()
    for j in range(3):
        s.add(C[i + 1][j] - C[i][j])
    if len(s) != 1:
        print('No')
        exit()

for j in range(2):
    s = set()
    for i in range(3):
        s.add(C[i][j + 1] - C[i][j])
    if len(s) != 1:
        print('No')
        exit()

print('Yes')