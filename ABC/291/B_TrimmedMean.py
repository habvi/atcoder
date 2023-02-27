N = int(input())
X = list(map(int, input().split()))

X.sort()
for _ in range(N):
    X.pop()

X.reverse()
for _ in range(N):
    X.pop()
print(sum(X) / (3 * N))
