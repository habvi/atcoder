n = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

d = []
for i, h in enumerate(H, 1):
    d.append((abs(A - (T - h * 0.006)), i))
d.sort()

print(d[0][-1])