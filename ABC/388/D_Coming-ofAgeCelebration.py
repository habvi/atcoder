N = int(input())
A = list(map(int, input().split()))

ac = [0] * (N + 1)
for i in range(N):
    A[i] += ac[i]
    right = N - i - 1
    pass_stone = min(A[i], right)
    ac[i + 1] += 1
    ac[i + pass_stone + 1] -= 1
    ac[i + 1] += ac[i]
    A[i] -= pass_stone
print(*A)
