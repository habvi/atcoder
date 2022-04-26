X = input()
n = int(input())
S = [input() for _ in range(n)]

d = {x : i for i, x in enumerate(X)}

S.sort(key=lambda x: [d[y] for y in x])
print(*S)