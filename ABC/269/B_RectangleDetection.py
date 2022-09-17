S = [input() for _ in range(10)]

ab, cd = set(), set()
for i in range(10):
    for j in range(10):
        if S[i][j] == '#':
            ab.add(i + 1)
            cd.add(j + 1)
print(min(ab), max(ab))
print(min(cd), max(cd))