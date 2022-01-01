n, k, m = map(int, input().split())
a = list(map(int, input().split()))
x = m*n - sum(a)
print(max(0, x) if k >= x else -1)