n = int(input())
A = sorted(map(int, input().split()))

print(sum(A) - A[0] - A[-1])