n, K = map(int, input().split())

m = n % K
print(min(m, K - m))