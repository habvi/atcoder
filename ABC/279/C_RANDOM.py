H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

s2 = list(zip(*S))
t2 = list(zip(*T))
s2.sort()
t2.sort()
print("Yes" if s2 == t2 else "No")