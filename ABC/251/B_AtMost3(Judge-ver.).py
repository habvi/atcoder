n, W = map(int, input().split())
A = list(map(int, input().split()))

s = set()
for i in range(n):
    x = A[i]
    if x <= W:
        s.add(x)
    for j in range(i + 1, n):
        x = A[i] + A[j]
        if x <= W:
            s.add(x)
        for k in range(j + 1, n):
            x = A[i] + A[j] + A[k]
            if x <= W:
                s.add(x)

print(len(s))