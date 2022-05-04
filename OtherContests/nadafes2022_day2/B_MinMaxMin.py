n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = max(A) * min(B)
for a, b in zip(A, B):
    ans = min(ans, a * b)
print(ans)