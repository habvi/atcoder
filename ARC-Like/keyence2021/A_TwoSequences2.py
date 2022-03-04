n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mx_a = 0
ans = 0
for a, b in zip(A, B):
    mx_a = max(mx_a, a)
    ans = max(ans, mx_a * b)
    print(ans)