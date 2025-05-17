N, K = map(int, input().split())
A = list(map(int, input().split()))

num = 1
for a in A:
    num *= a
    if len(str(num)) > K:
        num = 1
print(num)
