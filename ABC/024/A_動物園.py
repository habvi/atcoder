A, B, C, K = map(int, input().split())
S, T = map(int, input().split())

total = S + T
print(A * S + B * T - (total * C if total >= K else 0))