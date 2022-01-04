n = int(input())
g = [["."] * n for _ in range(n)]
for i in range(n):
    for j in range(2):
        if i + j < n:
            g[i][i + j] = "#"
    if i + 3 < n:
        g[i][i + 3] = "#"
        
for i in range(n - 3, n - 1):
    g[i][0] = "#"
for i in range(1, 3):
    g[n - 1][i] = "#"

for gg in g:
    print("".join(gg))