n, z, w = map(int, input().split())
A = list(map(int, input().split()))

if n == 1:
    print(abs(A[0] - w))
else:
    score1 = abs(A[-1] - w)
    score2 = abs(A[-1] - A[-2])
    print(max(score1, score2))