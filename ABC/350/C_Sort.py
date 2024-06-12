N = int(input())
A = list(map(int, input().split()))

d = {a: i for i, a in enumerate(A)}

ans = []
for xi in range(N):
    x = A[xi]
    yi = d[xi + 1]
    y = A[yi]
    if x == y or x == xi + 1:
        continue
    ans.append((xi + 1, yi + 1))
    A[xi], A[yi] = A[yi], A[xi]
    d[x] = yi
    d[y] = xi

print(len(ans))
for i, j in ans:
    print(i, j)
